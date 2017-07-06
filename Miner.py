from Block import Block
from Transaction import Transaction
import hashlib
from utils import *
import time
import pprint
import json

coinbase = Transaction(
        inputs=['coinbase'], 
        outputs=[{
            "toAddress":get_str_keys()['public'],
            "amount":calc_coinbase()
        }]
)

coinbase.sign_transaction()

transactions = [coinbase.to_dict()]

block = {
    "nonce":"",
    "proofOfWork":"",
    "transactions":transactions,
    "previous":"",
    "timestamp":""
}

nonce = 0
txhashes = [x['hash'] for x in transactions]
while True:
    difficulty = calc_difficulty()
    timeNow = time.time()
    hashes = ''.join(txhashes)
    plaintext = "{}{}{}".format(timeNow, nonce, hashes)
    hash = hashlib.sha512(plaintext.encode()).hexdigest()
    if hash.startswith("0" * difficulty):
        block['nonce'] = nonce
        block['timestamp'] = timeNow
        block['proofOfWork'] = hash
        block = Block(**block)
        pprint.pprint(block.__dict__)
        break
    nonce += 1
