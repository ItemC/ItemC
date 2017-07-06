import rsa
import json
import hashlib
import os
import random
import base64

def get_blockchain():
    if not os.path.exists(".data"):
        os.mkdir(".data")
    try:
        return json.load(open(".data/blockchain.json"))
    except:
        with open(".data/blockchain.json", 'w') as bc:
            bc.write("[]")
        return []

def calc_difficulty():
    # Temporary difficulty algorith: 1 - num_blocks / 1000
    return int((1 - len(get_blockchain()) / 1000.0) + 2)

def calc_coinbase():
    # Temporary coinbase algoithm 100 - (num_blocks / 1000) * 100
    return 100 - (len(get_blockchain()) / 1000) * 100

def load_public_key(key):
    key = "-----BEGIN RSA PUBLIC KEY-----\n{}\n-----END RSA PUBLIC KEY-----\n".format(key)
    return rsa.PublicKey.load_pkcs1(key.encode())    

def get_str_keys():
    keys = get_keys()
    pub = keys['public'].save_pkcs1().decode("utf8")
    priv = keys['private'].save_pkcs1().decode("utf8")
    pub = pub.replace("\n", '')
    priv = priv.replace("\n", '')
    pub = pub.replace("-----BEGIN RSA PUBLIC KEY-----", '').replace("-----END RSA PUBLIC KEY-----", '')
    priv = priv.replace("-----END RSA PRIVATE KEY-----", '').replace("-----BEGIN RSA PRIVATE KEY-----", '')
    return {
        "public":pub,
        "private":priv
    }
def generate_keys():
    """
        Essentially builds .data folder
    """
    pub,priv = rsa.newkeys(512)
    get_blockchain()

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

#DEGUG

def log(string):
    print(string)
