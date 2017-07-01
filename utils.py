import json
import hashlib
import os

def check_block(block_obj):
    hashString = "{}{}{}".format(block_obj.timestamp, ''.join(block_obj.transactions), block_obj.nonce) 
    theHash = hashlib.sha512(hashstring).hexdigest()
    if theHash != block_obj.proofOfWork:
        return False
    elif not block_obj.proofOfWork.startswith("0" * calc_difficulty()):
        return False
    
    blockchain = json.load(open("data_files/blockchain.json"))
    previous = blockchain[-1]['hash']
    if previous != block_obj.previous:
        return False
    return True

def calc_difficulty():
    # Temporary difficulty algorith: 1 - num_blocks / 1000
    bc = json.load(open("data_files/blockchain.json"))
    return 1 - len(bc) / 1000.0

def calc_coinbase():
    # Temporary coinbase algoithm 100 - (num_blocks / 1000) * 100
    return 100 - (num_blocks / 1000) * 100

