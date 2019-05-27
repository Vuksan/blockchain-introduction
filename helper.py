from bitcoin import random_key, privkey_to_address
from random import uniform
from model import Transaction

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
