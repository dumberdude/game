import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list('AELMORSUV')
        self.assertFalse(new_game.is_valid(""))
        self.assertFalse(new_game.is_valid("ABCDEFGHI"))
        self.assertFalse(new_game.is_valid("IZIPITAPO"))
        self.assertTrue(new_game.is_valid("MARVELOUS"))

    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to test
        self.assertIs(new_game.is_valid('FEUN'), False)
