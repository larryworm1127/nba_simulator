from unittest import TestCase


from stats.standing_data import get_data, find_indexes, rank_teams, create_standing_data
from stats.create_graph_data import *


class TestWinsLosses(TestCase):
    def test_get_data(self):
        season = '2016-17'
        print(get_data(season))
        data = get_data(season)
        for team_data in data:
            self.assertEqual(team_data[3], '2016-17')

        self.assertEqual(len(data), 30)

    def test_find_indexes(self):
        headings = ['TEAM_CITY', 'TEAM_NAME']
        with open(join(Main.TEAM_SEASON_PATH, 'ATL.json')) as data_file:
            parsed_json = load(data_file)

        result_sets = parsed_json['resultSets']
        self.assertEqual(find_indexes(result_sets, headings), [1, 2])

    def test_rank_teams(self):
        print(rank_teams('2016-17'))

    def test_create_standing_data(self):
        print(create_standing_data('2016-17'))
        print(create_standing_data('2017-18'))


class TestCreateStatsData(TestCase):
    def test_get_data(self):
        predicted_result = (
            [('ATL', 0.524), ('BKN', 0.244), ('BOS', 0.646), ('CHA', 0.439), ('CHI', 0.5), ('CLE', 0.622),
             ('DAL', 0.402),
             ('DEN', 0.488), ('DET', 0.451), ('GSW', 0.817), ('HOU', 0.671), ('IND', 0.512), ('LAC', 0.622),
             ('LAL', 0.317),
             ('MEM', 0.524), ('MIA', 0.5), ('MIL', 0.512), ('MIN', 0.378), ('NOP', 0.415), ('NYK', 0.378),
             ('OKC', 0.573),
             ('ORL', 0.354), ('PHI', 0.341), ('PHX', 0.293), ('POR', 0.5), ('SAC', 0.39), ('SAS', 0.744),
             ('TOR', 0.622),
             ('UTA', 0.622), ('WAS', 0.598)],
            [('ATL', 103.2), ('BKN', 105.8), ('BOS', 108.0), ('CHA', 104.9), ('CHI', 102.9), ('CLE', 110.3),
             ('DAL', 97.9),
             ('DEN', 111.7), ('DET', 101.3), ('GSW', 115.9), ('HOU', 115.3), ('IND', 105.1), ('LAC', 108.7),
             ('LAL', 104.6),
             ('MEM', 100.5), ('MIA', 103.2), ('MIL', 103.6), ('MIN', 105.6), ('NOP', 104.3), ('NYK', 104.3),
             ('OKC', 106.6),
             ('ORL', 101.1), ('PHI', 102.4), ('PHX', 107.7), ('POR', 107.9), ('SAC', 102.8), ('SAS', 105.3),
             ('TOR', 106.9),
             ('UTA', 100.7), ('WAS', 109.2)],
            [('ATL', 44.4), ('BKN', 43.9), ('BOS', 42.0), ('CHA', 43.6), ('CHI', 46.3), ('CLE', 43.7), ('DAL', 38.6),
             ('DEN', 46.4), ('DET', 45.7), ('GSW', 44.4), ('HOU', 44.4), ('IND', 42.0), ('LAC', 43.0), ('LAL', 43.5),
             ('MEM', 42.8), ('MIA', 43.6), ('MIL', 40.4), ('MIN', 42.4), ('NOP', 43.7), ('NYK', 45.2), ('OKC', 46.6),
             ('ORL', 43.1), ('PHI', 42.8), ('PHX', 45.0), ('POR', 43.6), ('SAC', 41.0), ('SAS', 43.9), ('TOR', 43.2),
             ('UTA', 43.2), ('WAS', 42.9)],
            [('ATL', 23.6), ('BKN', 21.4), ('BOS', 25.2), ('CHA', 23.1), ('CHI', 22.6), ('CLE', 22.7), ('DAL', 20.8),
             ('DEN', 25.3), ('DET', 21.1), ('GSW', 30.4), ('HOU', 25.2), ('IND', 22.5), ('LAC', 22.5), ('LAL', 20.9),
             ('MEM', 21.3), ('MIA', 21.2), ('MIL', 24.2), ('MIN', 23.7), ('NOP', 22.8), ('NYK', 21.8), ('OKC', 21.0),
             ('ORL', 22.2), ('PHI', 23.8), ('PHX', 19.6), ('POR', 21.1), ('SAC', 22.5), ('SAS', 23.8), ('TOR', 18.5),
             ('UTA', 20.1), ('WAS', 23.9)])

        actual_result = get_graph_data()
        self.assertEqual(actual_result, predicted_result)

    def test_top_ten(self):
        print(top_ten_rebounds())
        self.assertTrue(top_ten_rebounds())
        print(top_ten_wlr())
        self.assertTrue(top_ten_wlr())
        print(top_ten_assists())
        self.assertTrue(top_ten_assists())
        print(top_ten_points())
        self.assertTrue(top_ten_points())
