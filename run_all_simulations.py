import random
import matplotlib.pyplot as plt

def simulate_coin_tosses(n=100):
    heads = sum(1 for _ in range(n) if random.choice(['H', 'T']) == 'H')
    tails = n - heads
    plt.bar(['Heads', 'Tails'], [heads, tails], color=['blue', 'orange'])
    plt.title('Coin Toss Simulation (100 Tosses)')
    plt.ylabel('Count')
    for i, count in enumerate([heads, tails]):
        plt.text(i, count + 1, str(count), ha='center', va='bottom')
    plt.savefig('coin_toss.png')
    plt.close()

def simulate_rolling_dice(n=60):
    rolls = [random.randint(1, 6) for _ in range(n)]
    frequencies = {i: rolls.count(i) for i in range(1, 7)}
    outcomes = list(frequencies.keys())
    counts = list(frequencies.values())
    plt.bar(outcomes, counts, tick_label=outcomes)
    for i in range(len(outcomes)):
        plt.text(outcomes[i], counts[i] + 0.5, str(counts[i]), ha='center')
    plt.xlabel('Die Face')
    plt.ylabel('Frequency')
    plt.title('Frequency Distribution of Rolling a Six-Sided Die 60 Times')
    plt.savefig('rolling_dice.png')
    plt.close()

def simulate_drawing_cards(n=20):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(value, suit) for suit in suits for value in values]
    drawn_cards = [random.choice(deck) for _ in range(n)]
    red_count = sum(1 for card in drawn_cards if card[1] in ['Hearts', 'Diamonds'])
    black_count = n - red_count
    plt.bar(['Red', 'Black'], [red_count, black_count], color=['red', 'black'])
    plt.xlabel('Card Color')
    plt.ylabel('Count')
    plt.title('Count of Red vs Black Cards Drawn')
    for i, count in enumerate([red_count, black_count]):
        plt.text(i, count + 0.1, str(count), ha='center', va='bottom')
    plt.savefig('drawing_cards.png')
    plt.close()

def simulate_flipping_two_coins(n=50):
    flips = [(random.choice(['H', 'T']), random.choice(['H', 'T'])) for _ in range(n)]
    both_heads_count = sum(1 for flip in flips if flip == ('H', 'H'))
    at_least_one_head_count = sum(1 for flip in flips if 'H' in flip)
    labels = ['Both Heads', 'At Least One Head']
    counts = [both_heads_count, at_least_one_head_count]
    plt.bar(labels, counts, color=['blue', 'green'])
    for i, count in enumerate(counts):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')
    plt.xlabel('Outcome')
    plt.ylabel('Count')
    plt.title('Count of Coin Flip Outcomes')
    plt.savefig('compound_events.png')
    plt.close()

if __name__ == "__main__":
    simulate_coin_tosses()
    simulate_rolling_dice()
    simulate_drawing_cards()
    simulate_flipping_two_coins()