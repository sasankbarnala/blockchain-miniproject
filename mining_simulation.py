import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mineBlock(self, difficulty):
        prefix_str = '0' * difficulty
        start_time = time.time()
        attempts = 0

        while not self.hash.startswith(prefix_str):
            self.nonce += 1
            self.hash = self.compute_hash()
            attempts += 1

        end_time = time.time()
        print(f"✅ Block {self.index} successfully mined with difficulty {difficulty} using Proof of Work")
        print(f"Nonce found: {self.nonce}")
        print(f"Hash: {self.hash}")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {end_time - start_time:.4f} seconds\n")

def create_genesis_block():
    return Block(0, time.time(), "Genesis Block", "0")

def next_block(last_block, data):
    return Block(last_block.index + 1, time.time(), data, last_block.hash)

# Difficulty level (number of leading zeros required in hash)
difficulty = 4

# Initialize blockchain with genesis block
blockchain = [create_genesis_block()]
print("Mining Genesis Block...")
blockchain[0].mineBlock(difficulty)

# Mine additional blocks
for i in range(1, 3):
    new_block = next_block(blockchain[-1], f"Block {i} Data")
    print(f"Mining Block {i}...")
    new_block.mineBlock(difficulty)
    blockchain.append(new_block)
