# Example implementation of a blockchain in python
import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_passwords = ["GenesisBlock"]   
        self.mine_block(previous_hash=1) 

    def mine_block(self, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'passwords': self.current_passwords,
            'proof': 0,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_passwords = []
        self.chain.append(self.get_proof(block))
        return block

    def new_pass(self, password):
        self.current_passwords.append({
            "password": password
        })
        return self.last_bock["index"] + 1


    def get_proof(self, block):
        while self.validate_proof(block) is False:
            block["proof"] += 1
        return block

    def validate_proof(self, block):
        return self.hash(block)[:3] == "000"

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_bock(self):
        return self.chain[-1]

blockchain = Blockchain()
# print(blockchain.last_bock["proof"])
blockchain.new_pass("myPassword")
blockchain.new_pass("myNewPassword")
blockchain.mine_block()
for passwords in blockchain.last_bock["passwords"]:
    print(passwords.get("password"))
# print(blockchain.hash(blockchain.last_bock))
