import string
import random
import requests

EN_DICT = [
    "MARVELOUS",
    ]

class Game(object):

    dicturl = "https://wagon-dictionary.herokuapp.com"

    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        import pdb
        if not (len(word) >0 and len(word) <= 9):
            print("Word length must be > 0 and <= 9)")
            return False
        r = requests.get("{}/{}".format(self.dicturl, word))
        if not r.json()['found']:
            print("Word has not been found in the dictionnary")
            return False
        for letter in word.upper():
            if letter not in self.grid:
                print("Word's letter not found in the grid.")
                return False
        return True
