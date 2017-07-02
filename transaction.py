from utils import *
import hashlib
import json
import time
import uuid
import pprint

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
            self.signature = rsa.sign(self.hash, self.keys['public'], "SHA-1")
        else:
            raise Exception("Transaction already signed.")

    def verify_transaction(self):
        pass

    def is_spent(self):
        with open(".wallet/blockchain.json", 'r') as bc:
            pass

    def send(self):
        if not self.signature:
            raise Exception("Transaction is not signed.")
       
    def __str__(self):
        pprint.pprint({
            "hash":self.hash,
            "signature":self.signature,
            "inputs":self.inputs,
            "outputs":self.outputs
        })
