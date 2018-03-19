import datetime
from block import *

def create_genesis_block():
    # manually construct a block with index 0 and arbitrary previous hasher
    return Block(0, datetime.datetime.now(), "Genesis_Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now
    this_data = "Hey! I am block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


# ------- main ------- #

# Create the blockchain and add the genesis block_1
blockchain = [create_genesis_block()]
prev_block = blockchain[0]

# define the number of new blocks add to the blockchain
num_new_blocks = 10

# add blocks to the blockchain
for i in range(0, num_new_blocks):
    new_block = next_block(prev_block)
    blockchain.append(new_block)
    prev_block = new_block
    # tell everyone about it!
    print("Block #{} has been added to the blockchain!".format(new_block.index))
    print("Hash: {}\n".format(new_block.hash))
