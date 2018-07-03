import unittest
from os import environ

from stats_files import create_player_rating, create_team_list, get_id_from_abb, create_other_files

if not environ['CI']:
    class TestMain(unittest.TestCase):
        def test_create_team_list(self):
            self.assertTrue(create_team_list())

        def test_get_id_from_abb(self):
            self.assertEqual(get_id_from_abb('GSW'), '1610612744')


    class TestFileCheck(unittest.TestCase):
        def test_init(self):
            create_other_files.init()


class TestCreatePlayerRating(unittest.TestCase):
    def test_sort_player_into_team(self):
        self.assertTrue(create_player_rating.sort_player_into_team())


if __name__ == '__main__':
    unittest.main()
