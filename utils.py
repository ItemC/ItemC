from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Random import random
from Crypto import Random
import json
import hashlib
import os
import random
import base64

def check_block(blockObj):
    hashString = "{}{}{}".format(blockObj.timestamp, ''.join(blockObj.transactions), blockObj.nonce) 
    theHash = hashlib.sha512(hashstring).hexdigest()
    if theHash != blockObj.proofOfWork:
        return False
    elif not blockObj.proofOfWork.startswith("0" * calc_difficulty()):
        return False
    
    blockchain = json.load(open("data_files/blockchain.json"))
    previous = blockchain[-1]['hash']
    if previous != blockObj.previous:
        return False

    unverifiedTransactions = json.load("data_files/transactions")['unverified']
    for transaction in blockObj.transactions:
        # Verify signature of transactions
        pass    
    return True

def calc_difficulty():
    # Temporary difficulty algorith: 1 - num_blocks / 1000
    bc = json.load(open("data_files/blockchain.json"))
    return 1 - len(bc) / 1000.0

def calc_coinbase():
    # Temporary coinbase algoithm 100 - (num_blocks / 1000) * 100
    return 100 - (num_blocks / 1000) * 100

def generate_keys():
    key = RSA.generate(1024, e=random.choice(range(1,100001, 2)))
    pub = key.publickey().exportKey("DER")
    priv = key.exportKey("DER")
    pub = base64.b64encode(pub)
    priv = base64.b64encode(priv)
    return (pub, priv)

