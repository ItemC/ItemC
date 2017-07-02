from utils import *
import hashlib
import json
import time
import uuid
import pprint
import base64

class Transaction:
    def __init__(self, **kwargs):
        self.toAddr = kwargs['toAddr']
        self.fromAddr = kwargs['fromAddr']
        self.amount = kwargs['amount']
        self.inputs = kwargs['inputs']
        self.outputs = kwargs['outputs']
        if "hash" not in kwargs:
            self.hash = hashlib.sha1(str(self.inputs) + str(self.outputs)).hexdigest()
        else:
            self.hash = kwargs['hash']

        if "signature" not in kwargs:
            self.signature = None
        else:
            self.signature = kwargs['signature']

        self.keys = utils.get_keys()

    def sign_transaction(self):
        if not self.signature:
            self.signature = base64.b64encode(rsa.sign(self.hash, self.keys['public'], "SHA-1"))
        else:
            raise Exception("Transaction already signed.")

    def verify_transaction(self):
        check_hash = hashlib.sha1(str(self.inputs) + str(self.output)).hexdigest()
        if check_hash != self.hash:
            raise Exception("Transaction is invalid.")
        if self.is_spent():
            return Exception("Transaction is already spent.")
        if not rsa.verify(self.hash.encode(), base64.b64decode(self.signature), load_public_key(self.fromAddr)):
            return Exception("Invalid Signature")
        
    def is_spent(self):
        blocks = json.load(open(".data/blockchain.json"))
        for block in blocks:
            for i in block['inputs']:
                if i['hash'] == self.hash:
                    return True
        return False
    
    def send(self):
        if not self.signature:
            raise Exception("Transaction is not signed.")
    
        self.verify_transaction()
        if self.is_spent():
            raise Exception("Transaction is already spent")

        transaction = json.load(open(".data/transactions.json"))
        transaction['unverified'].append({
            "toAddr":self.toAddr,
            "fromAddr":self.fromAddr,
            "inputs":self.inputs,
            "output":self.outputs,
            "hash":self.hash,
            "signature":self.signature
        })
        with open(".data/transaction.json", 'w') as f:
            f.write(json.dumps(transaction))

    def __str__(self):
        pprint.pprint({
            "hash":self.hash,
            "signature":self.signature,
            "inputs":self.inputs,
            "outputs":self.outputs
        })
