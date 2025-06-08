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

    def __str__(self):
        return f"Block {self.index}:\n  Timestamp: {self.timestamp}\n  Data: {self.data}\n  Prev Hash: {self.previous_hash}\n  Hash: {self.hash}\n"

def create_genesis_block():
    return Block(0, time.time(), "Genesis Block", "0")

def next_block(last_block, data):
    index = last_block.index + 1
    timestamp = time.time()
    previous_hash = last_block.hash
    return Block(index, timestamp, data, previous_hash)

# Build the blockchain
blockchain = [create_genesis_block()]
blockchain.append(next_block(blockchain[-1], "Block 1 Data"))
blockchain.append(next_block(blockchain[-1], "Block 2 Data"))

print("🔗 Original Blockchain:")
for block in blockchain:
    print(block)

# Tamper with block 1's data
print("⚠️ Tampering Block 1...")
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].compute_hash()

print("🔍 Blockchain After Tampering Block 1:")
for block in blockchain:
    print(block)

def is_chain_valid(chain):
    for i in range(1, len(chain)):
        if chain[i].hash != chain[i].compute_hash():
            return False
        if chain[i].previous_hash != chain[i - 1].hash:
            return False
    return True


print("✅ Is Blockchain Valid?", is_chain_valid(blockchain))