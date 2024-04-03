import random 

suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

#cards = [r + s for r in ranks for s in suits]

cards = []
for s in suits:
    for r in ranks:
        cards.append(r+s)


random.shuffle(cards)

# hand = cards[:5] -> verwijdert de kaarten niet, pop wel
hand = [cards.pop() for _ in range(5)]

hand = []
for _ in range(5):
    hand.append(cards.pop())

print(f"Your hand contains: {", ".join(hand)}")
