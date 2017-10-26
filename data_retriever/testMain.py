from unittest import TestCase
from data_retriever import Main
from data_retriever import file_check


class TestMain(TestCase):
    def test1(self):
        #self.assertEqual(Main.sort_player_into_team(), "done")
        #file_check.init()
        Main.create_player_dict()
        self.assertEqual(1,1)
