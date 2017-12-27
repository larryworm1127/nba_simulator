from unittest import TestCase

import run_data_retrieve
from data_retriever import Main, create_player_rating, file_check


class TestMain(TestCase):
    def test_create_team_list(self):
        self.assertTrue(Main.create_team_list())

    def test_get_id_from_abb(self):
        self.assertEqual(Main.get_id_from_abb('GSW'), '1610612744')


class TestCreatePlayerRating(TestCase):
    def test_sort_player_into_team(self):
        self.assertTrue(create_player_rating.sort_player_into_team())


class TestFileCheck(TestCase):
    def test_init(self):
        file_check.init()
