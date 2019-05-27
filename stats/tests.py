# general imports
import unittest
from json import load
from os.path import join

from stats.graph_data import TEAM_SEASON_PATH, get_graph_data
from stats.standing_data import get_data, find_indexes, rank_teams, \
    create_standing_data
from stats.team_page_data import get_team_page_data, get_simulated_games


class TestWinsLosses(unittest.TestCase):
    def test_get_data(self):
        season = '2016-17'
        data = get_data(season)
        for team_data in data:
            self.assertEqual(team_data[3], '2016-17')

        self.assertEqual(len(data), 30)

    def test_find_indexes(self):
        headings = ['TEAM_CITY', 'TEAM_NAME']
        with open(join(TEAM_SEASON_PATH, 'ATL.json')) as data_file:
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


class TestCreateTeamPageData(unittest.TestCase):
    def test_get_games(self):
        self.assertTrue(get_team_page_data('ATL'))

    def test_get_simulated_game(self):
        self.assertTrue(get_simulated_games('ATL'))


if __name__ == '__main__':
    unittest.main()
