from unittest import TestCase
from season_games.create_team_page_data import get_games, data_cleanup


class TestCreateTeamPageData(TestCase):
    def test_get_games(self):
        print(get_games('ATL'))
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
