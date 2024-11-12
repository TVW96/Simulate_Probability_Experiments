import random
import matplotlib.pyplot as plt

# Step 1: Simulate rolling the die 60 times
rolls = [random.randint(1, 6) for _ in range(60)]

# Step 2: Count the frequency of each outcome
frequencies = {i: rolls.count(i) for i in range(1, 7)}

# Step 3: Print the frequency of each outcome
for outcome, frequency in frequencies.items():
    print(f"Outcome {outcome}: {frequency} times")

# Step 4: Plot the results
outcomes = list(frequencies.keys())
counts = list(frequencies.values())

plt.bar(outcomes, counts, tick_label=outcomes)
for i in range(len(outcomes)):
    plt.text(outcomes[i], counts[i] + 0.5, str(counts[i]), ha='center')
plt.xlabel('Die Face')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Rolling a Six-Sided Die 60 Times')
plt.show()
plt.savefig('rolling_dice.png')