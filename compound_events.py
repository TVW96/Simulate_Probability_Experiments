import random
import matplotlib.pyplot as plt

# Step 1: Simulate flipping two coins 50 times
flips = [(random.choice(['H', 'T']), random.choice(['H', 'T'])) for _ in range(50)]

# Step 2: Count the outcomes
both_heads_count = sum(1 for flip in flips if flip == ('H', 'H'))
at_least_one_head_count = sum(1 for flip in flips if 'H' in flip)

# Step 3: Plot the outcomes
labels = ['Both Heads', 'At Least One Head']
counts = [both_heads_count, at_least_one_head_count]

plt.bar(labels, counts, color=['blue', 'green'])
for i, count in enumerate(counts):
    plt.text(i, count + 0.5, str(count), ha='center', va='bottom')
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.title('Count of Coin Flip Outcomes')
plt.show()

plt.savefig('compund_events.png')