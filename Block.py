from utils import *
from hashlib import *
import json
import os
from Transaction import Transaction

class Block:
    def __init__(self, **kwargs):
        self.proofOfWork = kwargs['proofOfWork']
        self.nonce = kwargs['nonce']
        self.transactions = kwargs['transactions']
        self.previous = kwargs['previous']
        self.timestamp = kwargs['timestamp']
        if "hash"  not in kwargs:
            self.hash = self.create_block_hash()
        else:
            self.hash = kwargs['hash']
            
    def create_block_hash(self):
        plaintext = "{}{}{}{}".format(self.proofOfWork, self.nonce, self.previous, self.timestamp)
        for transaction in self.transactions:
            plaintext += transaction['hash']
        return sha1(plaintext.encode()).hexdigest()
        
    def verify_block(self):
        if not self.verify_proof_of_work():
            raise Exception("Invalid Proof of Work")
        if self.hash != self.create_block_hash():
            raise Exception("Invalid Hash")
        if not self.previous_exists():
            raise Exception("Previous block invalid")
        if len(self.transactions) < 1:
            raise Exception("Block must contain atleast one transaction")
        if not self.verify_transactions():
            raise Exception("Transactions are invalid")
        return True

    def block_exists(self):
        for block in get_blockchain():
            if block['hash'] == self.hash:
                return True
        return False

    def verify_proof_of_work(self):
        if not self.proofOfWork.startswith("0" * calc_difficulty()):
            return False
        txhashes = [x['hash'] for x in self.transactions]
        plaintext = "{}{}{}".format(self.timestamp, self.nonce, ''.join(txhashes))
        if self.proofOfWork != sha512(plaintext.encode()).hexdigest():
            return False
        return True

    def previous_exists(self):
        if self.hash == "751f6c75de62d987effab3bbfcbe14915158d886": # First block
            return True
        for block in get_blockchain():
            if block['hash'] == self.previous:
                return True
        return False

    def verify_transactions(self):
        for transaction in self.transactions:
            Transaction(**transaction).verify_transaction()
        return True
    
    def save_block(self):
        pass
