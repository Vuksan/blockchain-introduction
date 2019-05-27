from hashlib import sha256
import time
import datetime
from model import CandidateBlock, MinedBlock
from helper import generate_transactions

# mined("000345", "000") -> True
# mined("00345", "000") -> False
def mined(blockhash, target):
    return blockhash.startswith(target)

def mine(candidate_block, display_attempts=True):
    blockhash = ""
    nonce = 0

    # Measure elapsed time
    start_time = time.time()
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
        data_to_hash = candidate_block.previous_blockhash + str(candidate_block.timestamp) + str(nonce)
        hash_func = sha256(data_to_hash.encode('utf-8'))
        blockhash = hash_func.hexdigest()
        if display_attempts:
            print(blockhash, end='\n')  # print each attempt
        nonce += 1

    elapsed_time = time.time() - start_time
    print("\nMining time: " + str(datetime.timedelta(seconds=elapsed_time)))

    # We decrement nonce by one because at the end of the while loop we increment it one time too many
    return MinedBlock(candidate_block, blockhash, nonce-1)

def transmit_to_network(block):
    print("\nI found a new block, yay!\n")
    print(block)

def generate_genesis_block(target, transactions, height=0, display_attempts=True):
    candidate_block = CandidateBlock(
        height=height,
        previous_blockhash="674ccf292279cb232b613f5dc77041ce3da7e0fdfb20dfe9e4d190f05707a6b2", 
        timestamp=1506280816, 
        target=target,
        transactions=list()
    )
    return mine(candidate_block, display_attempts)

if __name__ == "__main__":
    target = input("Enter target: ") # Number of zeroes
    # Current bitcoin target is 0x000000000000000000CE4B00000018817F447F4768816FBB724DFB562A217126 (18 zeroes)

    # Generate several transactions
    transactions = generate_transactions(10)
    mined_block = generate_genesis_block(target, transactions)
    transmit_to_network(mined_block)
