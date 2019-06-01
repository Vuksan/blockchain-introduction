from hashlib import sha256
from time import time
from datetime import timedelta
from model import BlockHeader, CandidateBlock, MinedBlock, generate_transactions
from helper import hash_for_me, create_merkle_root

BLOCK_VERSION = "v1.0"

# mined("000345", "000") -> True
# mined("00345", "000") -> False
def mined(blockhash, target):
    return blockhash.startswith(target)

def mine(candidate_block, display_attempts=True):
    blockhash = ""
    block_header = candidate_block.block_header

    # Measure elapsed time
    start_time = time()
    # Mining algorithm (simplified example!):
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
    while True:
        data_to_hash = block_header.version + block_header.previous_blockhash \
            + str(block_header.timestamp) + block_header.merkle_root \
            + block_header.target + str(block_header.nonce)
        blockhash = hash_for_me(data_to_hash)
        if mined(blockhash, block_header.target):
            break
        if display_attempts:
            print(blockhash)  # print each attempt
        block_header.nonce += 1

    elapsed_time = time() - start_time
    print("\nMining time: %s" % timedelta(seconds=elapsed_time))

    # Return new, mined block
    return MinedBlock(candidate_block, blockhash)

def transmit_to_network(block):
    print("\nI found a new block, yay!\n")
    print(block)

def generate_genesis_block(target, height=0, starting_nonce=0, display_attempts=True):
    block_header = BlockHeader(BLOCK_VERSION, '', time(), '', target, starting_nonce)
    candidate_block = CandidateBlock(height, block_header, list())
    return mine(candidate_block, display_attempts)

if __name__ == "__main__":
    target = input("Enter target: ") # Number of zeroes
    # Current bitcoin target is 0x000000000000000000CE4B00000018817F447F4768816FBB724DFB562A217126 (18 zeroes)
    
    transactions = generate_transactions(10)
    merkle_root = create_merkle_root(transactions)
    block_header = BlockHeader(BLOCK_VERSION, '', time(), merkle_root, target, 0)
    candidate_block = CandidateBlock(0, block_header, transactions)
    mined_block = mine(candidate_block)
    transmit_to_network(mined_block)
