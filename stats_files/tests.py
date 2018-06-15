import unittest

from stats_files import files_main, create_player_rating, create_other_files

"""
TestMain test won't work until the nba_py package is fixed

class TestMain(unittest.TestCase):
    def test_create_team_list(self):
        self.assertTrue(files_main.create_team_list())

    def test_get_id_from_abb(self):
        self.assertEqual(files_main.get_id_from_abb('GSW'), '1610612744')
"""


class TestCreatePlayerRating(unittest.TestCase):
    def test_sort_player_into_team(self):
        self.assertTrue(create_player_rating.sort_player_into_team())


"""
TestFileCheck test won't work until nba_py package is fixed

class TestFileCheck(unittest.TestCase):
    def test_init(self):
        create_other_files.init()
"""

if __name__ == '__main__':
    unittest.main()
