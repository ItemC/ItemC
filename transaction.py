from utils import *
import hashlib
import json
import time
import uuid

class Transaction:
    def __init__(self, **kwargs):
        self.fromAddress = kwargs['fromAddress']
        self.toAddress = kwargs['toAddress']
        self.amount = kwargs['amount']
        # self.inputs 
        # self.outputs
        self.hash = get_hash(self) # Everyhting before gets hashed
        self.time = time.time()

    def send(self):
        if self.fromAddress == "coinbase":            
            with open("data_files/transactions.json") as readJson:
                transactionJson = json.loads(readJson.read())
                transactionJson['verified'].append(self.__dict__)
                transactionJson = json.dumps(transactionJson)
                open("data_files/transactions.json", 'w').write(transactionJson) 


if __name__ == "__main__":
    to = "pub"
    fromAddress="coinbase"
    amount = 5
    transaction = Transaction(
        toAddress=to,
        fromAddress=fromAddress,
        amount=amount
    )
    transaction.send()    
    
