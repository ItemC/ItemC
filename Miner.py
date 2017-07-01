from Block import Block
from Transaction import Transaction
import hashlib
from utils import *

coinbase = {
    "amount":Block.getCoinbase(),
    "fromAddress":"coinbase",
    "toAddress":"pub"
}

coinbaseTransaction = Transaction(**coinbase)

transactionsToConfirm = [coinbaseTransaction]
transactionHashes = ''.join([x.hash for x in sorted(transactionsToConfirm, key=lambda x: x.time)])

# sha512(<concatinated list of transaction hashes listed in order of time><nonce>)
while True:
    nonce = 0
    difficulty = Block.getDifficulty()
    hash = hashlib.sha512((str(transactionHashes) + str(nonce)).encode()).hexdigest()
    #print (hash, transactionHashes + str(nonce))
    if hash.encode("utf8").startswith(("0" * difficulty).encode()):
        print (hash, nonce)
        break
    nonce += 1

