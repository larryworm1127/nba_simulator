from unittest import TestCase
import data_retriever.Main as Main
import simulator.player_rating_machine as rating
import json

with open(Main.PLAYER_DICT_PATH, 'r') as player_dict_file:
    player_dict = json.load(player_dict_file)


class TestRatingMachine(TestCase):
    def test_rating(self):
        self.assertTrue(player_dict)
        self.assertTrue(rating.RatingMachine('201166'))  # Aaron Brooks
        self.assertTrue(rating.RatingMachine('201935'))  # James Harden
        self.assertTrue(rating.RatingMachine('201142'))  # Kevin Durant
        self.assertTrue(rating.RatingMachine('204001'))  # Porzingis
        self.assertTrue(rating.RatingMachine('201566'))  # Russell Westbrook
        self.assertTrue(rating.RatingMachine('203112'))
