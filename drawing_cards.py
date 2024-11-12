import random
import matplotlib.pyplot as plt

# Step 1: Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(value, suit) for suit in suits for value in values]

# Step 2: Draw 1 single card 20 times 
drawn_cards = [random.choice(deck) for _ in range(20)]

# Step 3: Count how many are red (Hearts and Diamonds)
red_count = sum(1 for card in drawn_cards if card[1] in ['Hearts', 'Diamonds'])
black_count = 20 - red_count

# Step 4: Print the counts
print(f"Red cards: {red_count}")
print(f"Black cards: {black_count}")

# Step 5: Plot the count of red versus black cards
labels = ['Red', 'Black']
counts = [red_count, black_count]
plt.bar(labels, counts, color=['red', 'black'])
plt.xlabel('Card Color')
plt.ylabel('Count')
plt.title('Count of Red vs Black Cards Drawn')
for i, count in enumerate(counts):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom')

plt.show()
plt.savefig('drawing_cards.png')