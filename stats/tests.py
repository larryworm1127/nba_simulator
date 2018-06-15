import unittest

from stats.standing_data import get_data, find_indexes, rank_teams, create_standing_data
from stats.graph_data import *


class TestWinsLosses(unittest.TestCase):
    def test_get_data(self):
        season = '2016-17'
        data = get_data(season)
        for team_data in data:
            self.assertEqual(team_data[3], '2016-17')

        self.assertEqual(len(data), 30)

    def test_find_indexes(self):
        headings = ['TEAM_CITY', 'TEAM_NAME']
        with open(join(files_main.TEAM_SEASON_PATH, 'ATL.json')) as data_file:
            parsed_json = load(data_file)

        result_sets = parsed_json['resultSets']
        self.assertEqual(find_indexes(result_sets, headings), [1, 2])

    def test_rank_teams(self):
        self.assertTrue(rank_teams('2016-17'))

    def test_create_standing_data(self):
        self.assertTrue(create_standing_data('2016-17'))
        self.assertTrue(create_standing_data('2017-18'))


class TestCreateStatsData(unittest.TestCase):
    def test_get_data(self):
        actual_result = get_graph_data()
        self.assertTrue(actual_result)

    def test_top_ten(self):
        self.assertTrue(top_ten_rebounds())
        self.assertTrue(top_ten_wlr())
        self.assertTrue(top_ten_assists())
        self.assertTrue(top_ten_points())


if __name__ == '__main__':
    unittest.main()
