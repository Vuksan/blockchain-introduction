from time import time
from random import randint
from model import CandidateBlock, MinedBlock, TransactionPool
from helper import generate_transactions
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
    transactions = generate_transactions(int(max_height) * MAX_TRANSACTIONS_PER_BLOCK)
    tx_pool = TransactionPool(transactions)

    # First create Genesis block (without transactions)
    mined_block = generate_genesis_block(target, list(), current_height, False)
    transmit_to_network(mined_block)
    current_height += 1

    # Populate the blockchain
    while current_height <= max_height:
        print("==================================================================================================")

        # Randomly determine number of transactions to take from transaction pool for this block
        tx_num = randint(MIN_TRANSACTIONS_PER_BLOCK, MAX_TRANSACTIONS_PER_BLOCK)
        include_txs = tx_pool.transactions[:tx_num]
        # Remove them from transaction pool
        tx_pool.transactions = tx_pool.transactions[tx_num+1:]
        tx_pool.transaction_num -= tx_num

        candidate_block = CandidateBlock(current_height, mined_block.blockhash, time(), target, include_txs)
        mined_block = mine(candidate_block, False)
        transmit_to_network(mined_block)

        current_height += 1