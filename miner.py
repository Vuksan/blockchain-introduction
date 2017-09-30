import hashlib

class UnminedBlock:
    def __init__(self, timestamp, previousblockhash, target):
        self.timestamp = timestamp
        self.previousblockhash = previousblockhash
        self.target = target

# In order to mine a block we need to find it's blockhash, and nonce
class MinedBlock:
    def __init__(self, unmined_block, blockhash, nonce):
        self.blockhash = blockhash
        self.timestamp = unmined_block.timestamp
        self.previousblockhash = unmined_block.previousblockhash
        self.nonce = nonce
        self.target = unmined_block.target
    
    def __repr__(self):
        return "Blockhash: %s, nonce: %s" % (self.blockhash, self.nonce)

# mined("000345", "000") -> True
# mined("00345", "000") -> False
def mined(blockhash, target):
    return blockhash.startswith(target)

def mine(unmined_block):
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
    while not mined(blockhash, unmined_block.target):
        data_to_hash = unmined_block.previousblockhash + str(unmined_block.timestamp) + str(nonce)
        hash_func = hashlib.sha256(data_to_hash)
        blockhash = hash_func.hexdigest()
        nonce += 1

    # We decrement nonce by one because at the end of the while loop we increment it one time too many
    return MinedBlock(unmined_block, blockhash, nonce-1)

def transmit_to_network(block):
    print "I found a new block, yay!"

if __name__ == "__main__":
    target = raw_input("Enter target: ")

    block = UnminedBlock(
        timestamp=1506280816, 
        previousblockhash="674ccf292279cb232b613f5dc77041ce3da7e0fdfb20dfe9e4d190f05707a6b2", 
        target=target
    )
    
    mined_block = mine(block)
    transmit_to_network(mined_block)
    print mined_block


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