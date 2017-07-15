from utils import *
import hashlib
import json
import time
import uuid
import pprint
import base64
import utils

class Transaction:
    def __init__(self, **kwargs):
        self.inputs = kwargs['inputs']
        self.outputs = kwargs['outputs']
        if not kwargs.get("hash"):
            self.hash = self.create_transaction_hash() 
        else:
            self.hash = kwargs['hash']

        if "signature" not in kwargs:
            self.signature = None
        else:
            self.signature = kwargs['signature']

        self.keys = utils.get_keys()

    def to_dict(self):
        return {
            "hash":self.hash,
            "signature":self.signature,
            "inputs":self.inputs,
            "outputs":self.outputs
        }

    def sign_transaction(self):
        if not self.signature:
            self.signature = base64.b64encode(rsa.sign(self.hash.encode(), self.keys['private'], "SHA-1")).decode()
        else:
            raise Exception("Transaction already signed.")

    def create_transaction_hash(self):
        plaintext = ""
        for input_ in self.inputs:
            plaintext += input_
        for output in self.outputs:
            plaintext += output['toAddress']
            plaintext += str(output['amount'])
        return hashlib.sha1(plaintext.encode()).hexdigest()
            
    def verify_transaction(self):
        checkHash = self.create_transaction_hash() 
        if checkHash != self.hash:
            raise Exception("Transaction hash is invalid.")
        if self.is_spent():
            return Exception("Transaction is already spent.")
        if not rsa.verify(self.hash.encode(), base64.b64decode(self.signature), load_public_key(self.outputs[0]['toAddress'])):
            return Exception("Invalid Signature")
        if not self.inputs_valid():
            return Exception("Inputs are invalid")
        if not self.outputs_valid():
            return Exception("Outputs are invalid")

    def inputs_valid(self):
        """
        Checks to see if input being used has not already been used
        """
        # Need to think about this more
        blockChain = utils.get_blockchain()
        for input_ in self.inputs:
            if input_ != "coinbase":
                for block in blockChain:
                    for transaction in block['transactions']:
                        for input_check in transaction['inputs']:
                            if input_check == input_:
                                return False
        return True                            

    def outputs_valid(self):
        """
        Checks that the amount in inputs is equal to amount in outputs.
        """
        blockChain = utils.get_blockchain()
        # Get price of inputs
        inputs_total = 0
        for input_ in self.inputs:
            for block in blockChain:
                for transaction in block['transactions']:
                    if input_ == transaction['hash']:
                        for output in transaction['outputs']:
                            if output['toAddress'] == self.keys['public']:
                                inputs_total += output['amount']
        outputs_total = 0
        for output in self.outputs:
            outputs_total += output['amount']
        if outputs_total != inputs_total:
            return False
        return True

    def is_spent(self):
        """
        Checks if this transaction is spent or not
        """
        blockChain = utils.get_blockchain()
        for block in blockChain:
            for transaction in block['transactions']:
                for input_ in transaction['inputs']:
                    if input_ == self.hash:
                        return True
        return False

    def send(self):
        if not self.signature:
            raise Exception("Transaction is not signed.")
    
        self.verify_transaction()
        if self.is_spent():
            raise Exception("Transaction is already spent")
        transaction = {
            "hash":self.hash,
            "signature":self.signature,
            "inputs":self.inputs,
            "outputs":self.outputs
        }

        # Send to network 
        return transaction

