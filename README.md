# Blockchain Mini Project

This repository contains three Python scripts demonstrating fundamental blockchain concepts and consensus mechanisms.

# Files Overview

# 1. `blockchain_simulation.py`
- Implements a basic blockchain with 3 linked blocks.
- Demonstrates how changing data in one block invalidates subsequent blocks.
- Shows the importance of hash chaining in blockchain integrity.

# 2. `mining_simulation.py`
- Simulates Proof-of-Work mining by finding a nonce such that the block hash starts with a given number of zeros (`difficulty`).
- Prints nonce attempts and time taken to mine each block.
- Illustrates computational effort involved in mining.

# 3. `consensus_demo.py`
- Simulates three consensus mechanisms:
  - Proof-of-Work (PoW): selects the miner with highest computational power.
  - Proof-of-Stake (PoS): selects the staker with highest stake.
  - Delegated Proof-of-Stake (DPoS): selects the delegate with most votes.
- Prints selected validators and explains each consensus logic.


# Requirements

- Python 3.x
- No external libraries required (uses only Python standard library)


# How to Run

Run each script independently using Python 3:

```bash
python3 blockchain_simulation.py
python3 mining_simulation.py
python3 consensus_demo.py
