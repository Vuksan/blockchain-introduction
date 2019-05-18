from hashlib import sha256

class Transaction:
    def __init__(self, address_from, address_to, amount):
        self.address_from = address_from
        self.address_to = address_to
        self.amount = amount
        # TXID is hash of a transaction data
        hash_func = sha256((self.address_from + self.address_to + str(self.amount)).encode('utf-8'))
        self.txid = hash_func.hexdigest()

    def __repr__(self):
        return "From: %s, To: %s, Amount: %s" % (self.address_from, self.address_to, self.amount)

class TransactionPool:
    def __init__(self, transactions):
        self.transaction_num = len(transactions)
        self.transactions = list(transactions)
    
    def __repr__(self):
        return "Number of transactions in the transaction pool: %s" %  self.transaction_num

class CandidateBlock:
    def __init__(self, height, previous_blockhash, timestamp, target, transactions):
        self.height = height
        self.previous_blockhash = previous_blockhash
        self.timestamp = timestamp
        self.target = target
        self.transactions = list(transactions)

# In order to mine a block we need to find it's blockhash, and nonce
class MinedBlock:
    def __init__(self, candidate_block, blockhash, nonce):
        self.height = candidate_block.height
        self.previous_blockhash = candidate_block.previous_blockhash
        self.timestamp = candidate_block.timestamp
        self.target = candidate_block.target
        self.transactions = list(candidate_block.transactions)
        self.blockhash = blockhash
        self.nonce = nonce
    
    def __repr__(self):
        output = "Height: %s\nBlockhash: %s\nNonce: %s\nPrevious blockhash: %s\n" % (self.height, self.blockhash, self.nonce, self.previous_blockhash)
        output += "Transactions:\n"
        for tr in self.transactions:
            output += "%s\n" % tr.txid
        return output