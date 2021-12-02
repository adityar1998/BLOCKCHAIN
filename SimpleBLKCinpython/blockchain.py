from hashlib import sha256
import json
import time


class chain:
    def __init__(self):
        self.blockchain = []
        self.pending = []
        self.add_block(prevhash="Genesis", proof=123)

    def add_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        self.pending.append(transaction)

    def compute_hash(self, block):
        json_block = json.dumps(block, sort_keys=True).encode()
        curhash = sha256(json_block).hexdigest()
        return curhash

    def add_block(self, proof, prevhash=None):
        block = {
            "index": len(self.blockchain),
            "timestamp": time.time(),
            "transactions": self.pending,
            "proof": proof,
            "prevhash": prevhash or self.compute_hash(self.blockchain[-1])
        }
        self.pending = []
        self.blockchain.append(block)


chain = chain()
t1 = chain.add_transaction("aditya", "satoshi", 100)
t2 = chain.add_transaction("ram", "aditya", 50)
t3 = chain.add_transaction("ram", "satoshi", 50)
chain.add_block(12345)
t1 = chain.add_transaction("aditya", "satoshi", 1000)
t2 = chain.add_transaction("ram", "aditya", 500)
t3 = chain.add_transaction("ram", "satoshi", 500)
chain.add_block(6789)
print(chain.blockchain)