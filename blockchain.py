from time import time
from datetime import timedelta
from random import randint
from model import BlockHeader, CandidateBlock, MinedBlock, generate_transactions
from helper import create_merkle_root
from miner import generate_genesis_block, mine, transmit_to_network

MIN_TRANSACTIONS_PER_BLOCK = 1
MAX_TRANSACTIONS_PER_BLOCK = 10

if __name__ == "__main__":
    max_height = int(input("Enter desired blockchain height: "))
    current_height = 0
    target = input("Enter target: ") # Number of zeroes
    # Current bitcoin target is 0x000000000000000000CE4B00000018817F447F4768816FBB724DFB562A217126 (18 zeroes)

    blockchain = list()
    # Initialize transaction (memory) pool
    transaction_pool = generate_transactions(max_height * MAX_TRANSACTIONS_PER_BLOCK)

    # Measure elapsed time until blockchain with desired height is created
    start_time = time()
    # First create Genesis block (without transactions)
    mined_block = generate_genesis_block(target=target, display_attempts=False)
    blockchain.append(mined_block)
    transmit_to_network(mined_block)
    current_height += 1

    # Populate the blockchain
    while current_height <= max_height:
        print("==================================================================================================")

        # Randomly determine number of transactions to take from transaction pool for this block
        tx_num_in_block = randint(MIN_TRANSACTIONS_PER_BLOCK, MAX_TRANSACTIONS_PER_BLOCK)
        include_txs = transaction_pool[:tx_num_in_block]
        # Remove them from transaction pool
        transaction_pool = transaction_pool[tx_num_in_block+1:]

        merkle_root = create_merkle_root(include_txs)
        block_header = BlockHeader(mined_block.block_header.version, mined_block.blockhash, time(), merkle_root, target, 0)
        candidate_block = CandidateBlock(current_height, block_header, include_txs)
        mined_block = mine(candidate_block, False)
        blockchain.append(mined_block)
        transmit_to_network(mined_block)

        current_height += 1

    elapsed_time = time() - start_time
    print("\nBlockchain creation time: " + str(timedelta(seconds=elapsed_time)))
