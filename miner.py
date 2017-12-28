from __future__ import print_function
import hashlib
import time
import datetime

class CandidateBlock:
    def __init__(self, previousblockhash, timestamp, target):
        self.previousblockhash = previousblockhash
        self.timestamp = timestamp
        self.target = target

# In order to mine a block we need to find it's blockhash, and nonce
class MinedBlock:
    def __init__(self, candidate_block, blockhash, nonce):
        self.previousblockhash = candidate_block.previousblockhash
        self.timestamp = candidate_block.timestamp
        self.target = candidate_block.target
        self.nonce = nonce
        self.blockhash = blockhash
    
    def __repr__(self):
        return "Blockhash: %s, nonce: %s" % (self.blockhash, self.nonce)

# mined("000345", "000") -> True
# mined("00345", "000") -> False
def mined(blockhash, target):
    print('.', end='')   # print a dot for each attempt
    return blockhash.startswith(target)

def mine(candidate_block):
    blockhash = ""
    nonce = 0

    # Mining algorithm (simplified!):
    #
    # blockhash = sha256(previousblockhash + timestamp + nonce)
    # 23tea1... = 674ccf...7a6b2 + 1506280816 + 0
    # 34tuyu... = 674ccf...7a6b2 + 1506280816 + 1
    # 124saD... = 674ccf...7a6b2 + 1506280816 + 2
    # ...
    # 0007ff... = 674ccf...7a6b2 + 1506280816 + 2875
    #
    # Success!
    #
    # So our nonce is 2875, and the blockhash is 0007ff67d9f21a7e153ee92fad6336a1e395c94db1a87221b4aca48507213b98
    # (we can omit zeroes = 7ff67d9f21a7e153ee92fad6336a1e395c94db1a87221b4aca48507213b98) 
    while not mined(blockhash, candidate_block.target):
        data_to_hash = candidate_block.previousblockhash + str(candidate_block.timestamp) + str(nonce)
        hash_func = hashlib.sha256(data_to_hash)
        blockhash = hash_func.hexdigest()
        nonce += 1

    # We decrement nonce by one because at the end of the while loop we increment it one time too many
    return MinedBlock(candidate_block, blockhash, nonce-1)

def transmit_to_network(block):
    print("\nI found a new block, yay!")

if __name__ == "__main__":
    target = raw_input("Enter target: ") # Number of zeroes
    # Current bitcoin target is 0x000000000000000000CE4B00000018817F447F4768816FBB724DFB562A217126 (18 zeroes)

    block = CandidateBlock(
        previousblockhash="674ccf292279cb232b613f5dc77041ce3da7e0fdfb20dfe9e4d190f05707a6b2", 
        timestamp=1506280816, 
        target=target
    )
    
    # Measure elapsed time
    start_time = time.time()

    mined_block = mine(block)
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    transmit_to_network(mined_block)
    print(mined_block)
    print("Elapsed time: " + str(datetime.timedelta(seconds=elapsed_time)))


### FAQ ###

# What is target?
#
# - Target is simply a number of zeroes with which the mined blockhash needs to start with in order for the mining to succeed.

# Why are there no zeroes in front of a blockhash then?
#
# - There are, but they are omitted.

# What is nonce?
#
# - The nonce is a 32-bit field whose value we constantly change until we "win the lottery" and mine new block
# (we increment it from 0 in this example).

# What happens if 2 miners mine the same block at the same time?
#
# - When 2 blocks are generated at the same time, the agreement on which block is the "winner" depends on the next block.
# The community agrees on the "longest" chain. Sometimes there are multiple chains of equal length, 
# and that's why it can be important to wait for a number of block confirmations, 
# before considering that a transaction will not be undone by a chain reorganization.

# Is target always the same?
#
# - No, it changes (every x blocks) depending on how fast or slow the network was until that point.

# So python cannot be used with the blockchain?
#
# - Sure it can, in fact many blockchain applications are written in python,
# the most popular being bitcoin electrum wallet.