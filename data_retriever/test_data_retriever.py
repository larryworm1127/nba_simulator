from unittest import TestCase
from data_retriever import Main, create_player_rating


class TestMain(TestCase):
    def test_create_team_list(self):
        Main.create_team_list()


class TestCreatePlayerRating(TestCase):
    def test_sort_player_into_team(self):
        self.assertTrue(create_player_rating.sort_player_into_team())
