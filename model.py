from bitcoin import random_key, privkey_to_address
from random import uniform
from copy import deepcopy
from helper import hash_for_me

class Transaction:
    def __init__(self, address_from, address_to, amount):
        self.address_from = address_from
        self.address_to = address_to
        self.amount = amount
        # TXID represents the hash of a transaction data
        self.txid = hash_for_me(self.address_from + self.address_to + str(self.amount))

    def __repr__(self):
        return "From: %s, To: %s, Amount: %s" % (self.address_from, self.address_to, self.amount)

# Generates and returns a list of random transactions
def generate_transactions(num=1):
    transactions = list()
    for _ in range(num):
        # First generate private keys
        private_key_from = random_key()
        private_key_to = random_key()
        # Convert them to bitcoin addresses
        address_from = privkey_to_address(private_key_from)
        address_to = privkey_to_address(private_key_to)
        # Generate some amount
        amount = round(uniform(0.1, 10), 8)
        transactions.append(Transaction(address_from, address_to, amount))
    return transactions

class BlockHeader:
    def __init__(self, version, previous_blockhash, timestamp, merkle_root, target, starting_nonce):
        self.version = version
        self.previous_blockhash = previous_blockhash
        self.timestamp = timestamp
        self.merkle_root = merkle_root
        self.target = target
        self.nonce = starting_nonce

class CandidateBlock:
    def __init__(self, height, block_header, transactions):
        self.height = height
        self.block_header = deepcopy(block_header)
        self.transactions = list(transactions)

class MinedBlock:
    def __init__(self, candidate_block, blockhash):
        self.height = candidate_block.height
        self.block_header = deepcopy(candidate_block.block_header)
        self.blockhash = blockhash
        self.transactions = list(candidate_block.transactions)
    
    def __repr__(self):
        output = "Height: %s\nBlockhash: %s\nNonce: %s\nPrevious blockhash: %s\n" % (self.height, self.blockhash, self.block_header.nonce, self.block_header.previous_blockhash)
        output += "Transactions:\n"
        for tr in self.transactions:
            output += "%s\n" % tr.txid
        return output
