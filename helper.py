from hashlib import sha256

def hash_for_me(data):
    tmp = sha256(data.encode('utf-8'))
    return tmp.hexdigest()

# Simplified, not correct, merkle root generation process
def create_merkle_root(transactions):
    data_to_hash = ""
    for tr in transactions:
        data_to_hash += tr.txid
    return hash_for_me(data_to_hash)
