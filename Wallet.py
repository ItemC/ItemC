from transaction import *
from Blockchain import *

class Wallet:

    
    def __init__(self, key):
        self.publicKey = key
        self.transactions = []
        self.bchain = Blockchain()

    def get_balance(self):
        transactions = self.bchain.get_unspend_transactions_for_adress(key)

        balance = 0
        for t in transactions:
            if t.toAddress == publicKey: 
                balance += amount    
            if t.fromAddress == publicKey:
                balance -= amount
