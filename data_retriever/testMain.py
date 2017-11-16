from unittest import TestCase
from data_retriever import Main


class TestMain(TestCase):
    def test_sort_player(self):
        Main.sort_player_into_team()

    def test_create_team_list(self):
        Main.create_team_list()
