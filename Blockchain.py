from utils import *
from hashlib import *
import json
import time

class Blockchain:
    def __init__(self, **kwargs):
        self.proofOfWork = kwargs['proofOfWork']
        self.nonce = kwargs['nonce']
        self.transactions = kwargs['transactions']
        self.previous = kwargs['previous']
        self.hash = get_hash(self)
        self.time = time.time()

    def saveBlock(self):
        self.checkBlock()
        with open("data_files/blockchain.json", 'r') as readData:
            data = json.loads(readData.read())
            data[self.hash] = self.__dict__
            open("data_files/blockchain.json", 'w').write(json.dumps(data))

    def checkBlock(self):
        if not self.proofOfWork.startswith("0" * self.getDifficulty()):
            raise Exception("Hash not valid. Incorrect number of leading zeros")
        sorted_transactions = sorted(self.transactions, key=lambda x: x.time)
        transaction_sig = ''.join([x.hash for x in sorted_transactions])
        hash_value = transaction_sig + str(self.nonce)
        hash = hashlib.sha512(hash_value).hexdigest()
        if hash != self.proofOfWork:
            raise Exception("Invalid proot of work")
        
    @staticmethod
    def getDifficulty(self=None):
        return 4

    @staticmethod
    def getCoinbase(self=None):
        return 25

