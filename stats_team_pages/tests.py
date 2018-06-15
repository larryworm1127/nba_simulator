import unittest

from stats_team_pages.team_page_data import get_games, data_cleanup, get_simulated_games


class TestCreateTeamPageData(unittest.TestCase):
    def test_get_games(self):
        self.assertTrue(get_games('ATL'))

    def test_display_cleanup(self):
        ori_data = [1610612737, '0021601177', 'APR 06, 2017', 'ATL vs. BOS', 'W', 40, 38, 0.513, 240, 44, 89, 0.494, 11,
                    23, 0.478, 24, 34, 0.706, 13, 39, 52, 26, 7, 4, 17, 30, 123]
        ori_header = ['Team_ID', 'Game_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA',
                      'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL',
                      'BLK', 'TOV', 'PF', 'PTS']
        shorten_data = (['W', 40, 38, 13, 39, 52, 26, 7, 4, 17, 30, 123],
                        ['WL', 'W', 'L', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'])

        self.assertEqual(data_cleanup(ori_header, ori_data), shorten_data)

    def test_get_simulated_game(self):
        self.assertTrue(get_simulated_games('ATL'))


if __name__ == '__main__':
    unittest.main()
