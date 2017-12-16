from json import load
from unittest import TestCase

from os.path import join

from data_retriever import Main
from stats.standing_data import get_data, find_indexes, rank_teams, create_standing_data


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
