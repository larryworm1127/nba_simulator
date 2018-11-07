# general imports
import unittest
from json import load
from os.path import join

from stats.standing_data import get_data, find_indexes, rank_teams, \
    create_standing_data
from stats.graph_data import TEAM_SEASON_PATH, get_graph_data, \
    top_ten_rebounds, top_ten_wlr, top_ten_assists, top_ten_points
from stats.team_page_data import get_games, data_cleanup, get_simulated_games


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

    def test_top_ten(self):
        self.assertTrue(top_ten_rebounds())
        self.assertTrue(top_ten_wlr())
        self.assertTrue(top_ten_assists())
        self.assertTrue(top_ten_points())


class TestCreateTeamPageData(unittest.TestCase):
    def test_get_games(self):
        self.assertTrue(get_games('ATL'))

    def test_display_cleanup(self):
        ori_data = [1610612737, '0021601177', 'APR 06, 2017', 'ATL vs. BOS',
                    'W', 40, 38, 0.513, 240, 44, 89, 0.494, 11,
                    23, 0.478, 24, 34, 0.706, 13, 39, 52, 26, 7, 4, 17, 30, 123]
        ori_header = ['Team_ID', 'Game_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'W',
                      'L', 'W_PCT', 'MIN', 'FGM', 'FGA',
                      'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA',
                      'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL',
                      'BLK', 'TOV', 'PF', 'PTS']
        shorten_data = (['W', 40, 38, 13, 39, 52, 26, 7, 4, 17, 30, 123],
                        ['WL', 'W', 'L', 'OREB', 'DREB', 'REB', 'AST', 'STL',
                         'BLK', 'TOV', 'PF', 'PTS'])

        self.assertEqual(data_cleanup(ori_header, ori_data), shorten_data)

    def test_get_simulated_game(self):
        self.assertTrue(get_simulated_games('ATL'))


if __name__ == '__main__':
    unittest.main()
