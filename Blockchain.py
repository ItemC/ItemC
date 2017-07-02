from Block import *
import json
from Transaction
import time
class Blockchain:
    def __init__(self):
        self.blocks = self.load_from_file()

    #the blockchain gets compleatly loaded into ram when using it. (for now) this is why there is loading and saving. Although blcoks already support singe loading/saving
    def write_to_file(self, pathToDirectory):
        #takes all the blocks and writes them to a path (as JSON for now)
        for b in self.blocks:
            b.write_block()

    def load_from_file(self, pathToDirectory = None):
        #loads the blocks array from a json
        if pathToDirectory:
            self.blocks = json.load(open(pathToDirectory))
        else:
            self.blocks = json.load(open(".data/blockchain"))
        for block in self.blocks:
            block = Block(**block)
            for transaction in block.transactions:
                
    def is_spend(self, transaction):
        for block in self.blocks:
            for t in block['transactions']:
                for i in t['inputs']:
                    if i['hash'] == self.hash:
                        return True
        return False
    
    def is_transaction_spent(self, transaction):
        
        #debug
        timestamp = time.time()
        for b in self.blocks:
            for t in b.transaction:
                if i in t.inputs:
                    if i['txhash'] == t.hash:
                        return True
        utils.log("checking of transaction_is_spend took: {}".format(time.time() - timestamp))
        return False

    def get_unspend_transactions_for_address(self, address):
        allTransactions = []
        for b in self.blocks:
            allTransactions.append(b.transactions)
        
        transactionsWithAddress = list(filter(lambda transaction: (transaction.fromAddress == address or transaction.toAdress == address), allTransactions))


        def not_used_as_input(transaction):
            for t in allTransactions:
                if transaction in t.inputs:
                    return True
            return False
        unspendTransactionsWithAdress = list(filter(lambda transaction: not_used_as_input(transaction), transactionsWithAddress))
        return unspendTransactionsWithAdress