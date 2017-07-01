from transaction import *
from Blockchain import *

class Wallet:
    publicKey = ""
    transactions = []
    def __init__(key):
        publicKey = key

    def get_balance():
        transactions = Blockchain.get_unspend_transactions_for_adress(key)

        balance = 0
        for t in transactions:
            if t.toAddress == publicKey: 
                balance += amount    
            if t.fromAddress == publicKey:
                balance -= amount
