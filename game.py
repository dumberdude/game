import string
import random

EN_DICT = [
    "MARVELOUS",
    ]

class Game(object):
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not (len(word) >0 and len(word) <= 9):
            return False
        if word not in EN_DICT:
            return False
        return True
