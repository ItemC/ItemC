from utils import get_blockchain
from Block import Block

block = get_blockchain()[0]
block = Block(**block)
print(block.verify_block())
