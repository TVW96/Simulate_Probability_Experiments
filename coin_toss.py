import random 
import matplotlib.pyplot as plt

# Step 1: Simulate 100 coin tosses
def simulate_coin_tosses(n=100):
    heads = sum(1 for _ in range(n) if random.choice(['H', 'T']) == 'H')
    tails = n -heads
    return heads, tails

# Step 2: Run simulation
heads, tails = simulate_coin_tosses()

# Step 3: Plot results
plt.bar(['Heads', 'Tails'], [heads, tails], color=['blue', 'orange'])
plt.title('Coin Toss Simulation (100 Tosses)')
plt.ylabel('Count')
for i, count in enumerate([heads, tails]):
    plt.text(i, count + 1, str(count), ha='center', va='bottom')

plt.show()
plt.savefig('coin_toss.png')
