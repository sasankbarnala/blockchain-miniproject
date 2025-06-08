import random
from collections import Counter

# --- Setup mock validators ---

# PoW miners with computational power
miners = [
    {"id": "Miner1", "power": random.randint(1, 100)},
    {"id": "Miner2", "power": random.randint(1, 100)},
    {"id": "Miner3", "power": random.randint(1, 100)},
]

# PoS stakers with stakes
stakers = [
    {"id": "Staker1", "stake": random.randint(100, 1000)},
    {"id": "Staker2", "stake": random.randint(100, 1000)},
    {"id": "Staker3", "stake": random.randint(100, 1000)},
]

# DPoS voters voting for delegates
voters = [
    {"voter": "Voter1", "vote": random.choice(["Delegate1", "Delegate2", "Delegate3"])},
    {"voter": "Voter2", "vote": random.choice(["Delegate1", "Delegate2", "Delegate3"])},
    {"voter": "Voter3", "vote": random.choice(["Delegate1", "Delegate2", "Delegate3"])},
]

print("=== Consensus Simulation ===\n")

# PoW: Miner with highest power wins
pow_winner = max(miners, key=lambda x: x["power"])
print(f"PoW: Miner selected is {pow_winner['id']} with power {pow_winner['power']}")
print("Explanation: Miner with the highest computational power wins the right to add the next block.\n")

# PoS: Staker with highest stake wins
pos_winner = max(stakers, key=lambda x: x["stake"])
print(f"PoS: Staker selected is {pos_winner['id']} with stake {pos_winner['stake']}")
print("Explanation: Validator with the highest stake is chosen to forge the next block.\n")

# DPoS: Delegate with most votes wins
votes = [v['vote'] for v in voters]
vote_counts = Counter(votes)
dpos_winner, votes_received = vote_counts.most_common(1)[0]

print(f"DPoS: Delegate selected is {dpos_winner} with {votes_received} votes")
print("Votes breakdown:", dict(vote_counts))
print("Explanation: Voters elect delegates who validate blocks on their behalf.\n")
