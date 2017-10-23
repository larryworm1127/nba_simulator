from unittest import TestCase
import data_retriever.Main as Main


class TestMain(TestCase):
    def test_sort_player_into_team(self):
        self.assertEqual(Main.sort_player_into_team(), "done")
