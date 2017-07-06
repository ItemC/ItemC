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
        self.timestamp = time.time()
        if "hash" not in kwargs:
            self.hash = self.create_transaction_hash() 
        else:
            self.hash = kwargs['hash']

        if "signature" not in kwargs:
            self.signature = None
        else:
            self.signature = kwargs['signature']

        self.keys = utils.get_keys()

    def sign_transaction(self):
        if not self.signature:
            self.signature = base64.b64encode(rsa.sign(self.hash.encode(), self.keys['private'], "SHA-1"))
        else:
            raise Exception("Transaction already signed.")

    def create_transaction_hash(self):
        concatinatedString = "{}".format(self.timestamp)
        for input_ in self.inputs:
            concatinatedString += input_
            #concatinatedString += input_['txhash']
            #concatinatedString += str(input_['outputIndex'])
        for output in self.outputs:
            concatinatedString += output['toAddress']
            concatinatedString += str(output['amount'])
        return hashlib.sha1(concatinatedString.encode()).hexdigest()
            
    def verify_transaction(self):
        checkHash = self.create_transaction_hash() 
        if checkHash != self.hash:
            raise Exception("Transaction is invalid.")
        if self.is_spent():
            return Exception("Transaction is already spent.")
        if not rsa.verify(self.hash.encode(), base64.b64decode(self.signature), load_public_key(self.outputs[0]['toAddress'])):
            return Exception("Invalid Signature")
        if not self.inputs_valid():
            return Exception("Inputs are invalid")

    def inputs_valid(self):
        # Need to think about this more
        blockChain = utils.get_blockchain()
        return True                            

    def is_spent(self):
        blockChain = utils.get_blockchain()
        for block in blockChain:
            for transaction in block['transactions']:
                for input_ in transaction['inputs']:
                    if input_['hash'] == self.hash:
                        return True
        return False

    def send(self):
        if not self.signature:
            raise Exception("Transaction is not signed.")
    
        self.verify_transaction()
        if self.is_spent():
            raise Exception("Transaction is already spent")

        # Send to network 
        return {
            "hash":self.hash,
            "signature":self.signature,
            "timestamp":self.timestamp,
            "inputs":self.inputs,
            "outputs":self.outputs
        }

