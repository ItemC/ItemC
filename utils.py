import rsa
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
    pub,priv = rsa.newkeys(512)
    os.mkdir(".data")
    with open(".data/pub.key", 'w') as pubF:
        with open(".data/priv.key", 'w') as privF:
            pubF.write(pub.save_pkcs1().decode("utf8"))
            privF.write(priv.save_pkcs1().decode("utf8"))
    return {"public":pub, "private":priv}

def get_keys():
    if not os.path.exists(".data/pub.key") or not os.path.exists(".data/priv.key"):
        generate_keys()
    with open(".data/pub.key", 'r') as f:
        pub = rsa.PublicKey.load_pkcs1(f.read())
    with open(".data/priv.key", 'r') as f:
        priv = rsa.PrivateKey.load_pkcs1(f.read())
    return {"public":pub, "private":priv}
