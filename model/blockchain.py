# Example implementation of a blockchain in python
import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_passwords = []   
        self.new_block(proof=1, previous_hash=1) 

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'passwords': self.current_passwords,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_passwords = []
        self.chain.append(block)
        return block

    def new_pass(self, password):
        sef.current_passwords.append{
            "password": password
        }
        return self.last_bock['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_bock(self):
        return self.chain[-1]

