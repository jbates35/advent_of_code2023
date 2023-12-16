import time
import numpy as np

hands = []

score_matrix = {"T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}

with open("data.txt", "r") as f:
    for line in f:
        hand_score = 0
        hand_items = line.split()

        unique_card_dict = {}

        for i, card in enumerate(hand_items[0]):
            if card in score_matrix:
                card = score_matrix[card]
            hand_score += int(card) * 16 ** (9 - i)

            if card in unique_card_dict:
                unique_card_dict[card] += 1
            else:
                unique_card_dict[card] = 1

        unique_cards = [
            card for card in sorted(unique_card_dict.values(), reverse=True)
        ]

        if unique_cards[0] == 5:
            rank_score = 6
        elif unique_cards[0] == 4:
            rank_score = 5
        elif unique_cards[0] == 3 and unique_cards[1] == 2:
            rank_score = 4
        elif unique_cards[0] == 3:
            rank_score = 3
        elif unique_cards[0] == 2 and unique_cards[1] == 2:
            rank_score = 2
        elif unique_cards[0] == 2:
            rank_score = 1
        else:
            rank_score = 0

        hand_score += rank_score * 16**10
        hand_score += int(hand_items[1])
        hands += [hand_score]

# numpy this
timer = time.time()
total_score = 0
for i, hand in enumerate(sorted(hands, reverse=True)):
    total_score += (hand & 0xFFFFF) * (i + 1)
print(f"total score from for loop is {total_score}")
print(f"time taken is {time.time() - timer}")

print("\n")

timer = time.time()
hands_np = np.array(sorted(hands, reverse=True))
hands_np = hands_np & 0xFFFFF
total_score = np.sum(hands_np * (np.arange(len(hands_np)) + 1))
print(f"total score from np loop is {total_score}")
print(f"time taken is {time.time() - timer}")
