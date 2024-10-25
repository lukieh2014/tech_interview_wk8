"""Scrabble game in Python"""
import random

def get_score_for_word(word: str) -> int:
    LETTER_SCORES = {"E": 1, "A": 1, "I": 1, "O": 1,
                 "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1, "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
                 "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}
    score = 0
    for letter in word:
        score += LETTER_SCORES[letter]

    return score

def give_seven_tiles() -> list:
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

    player_hand = []
    for _ in range(7):
        card = random.choice(alphabet)
        player_hand.append(card)
    
    return player_hand
    

def generate_player_rack() -> list:
    TILES_DISTRIBUTION = {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6, "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2,
                      "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2, "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1}
    player_rack = []
    # for i in range(7):
    while len(player_rack) < 7:
        card = random.choice(list(TILES_DISTRIBUTION.keys()))
        TILES_DISTRIBUTION[card] -= 1
        if TILES_DISTRIBUTION[card] == 0:
            TILES_DISTRIBUTION.pop(card)

        player_rack.append(card)
    
    print(player_rack)
    return player_rack

if __name__ == "__main__":
    print(get_score_for_word(""))
    generate_player_rack()
