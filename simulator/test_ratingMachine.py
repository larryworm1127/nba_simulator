from unittest import TestCase
import data_retriever.Main as Main
import simulator.player_rating_machine as rating


class TestRatingMachine(TestCase):
    def test_rate(self):
        print(Main.player_dict)
        self.assertTrue(Main.player_dict)
        self.assertTrue(rating.RatingMachine(201166))  # Aaron Brooks
        self.assertTrue(rating.RatingMachine(201935))  # James Harden
        self.assertTrue(rating.RatingMachine(201142))  # Kevin Durant
        self.assertTrue(rating.RatingMachine(204001))  # Porzingis
        self.assertTrue(rating.RatingMachine(201566))  # Russell Westbrook
