from utils import *
from hashlib import *
import json
import os

class Block:
    def __init__(self, **kwargs):
        self.proofOfWork = kwargs['proofOfWork']
        self.nonce = kwargs['nonce']
        self.transactions = kwargs['transactions']
        self.previous = kwargs['previous']
        self.timestamp = kwargs['timestamp']
        self.hash = self.get_hash()

    def get_hash(self):
        transactionHashes = ''.join(self.transactions)
        hashString = transactionHashes + self.proofOfWork + self.nonce + self.previous + str(self.timestamp)
        return sha1(hashstring).hexdigest()

    def write_block(self):
        if not os.path.exists("data_files/blockchain.json"):
            with open("data_files/blockchain.json", 'w') as bc:
                bc.write(json.dumps([
                    self.__dict__  
                ]))
        else:
            current_json = json.load(open("data_files/blockchain.json"))
            current_json.append(json.dumps(self.__dict__))

