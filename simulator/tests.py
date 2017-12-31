from unittest import TestCase
from simulator.single_player_rating import SinglePlayerRating
from simulator.run_season_simulation import run_simulation
from simulator.one_game_simulation import GameSimulation
from simulator.run_playoff_simulation import *
from simulator.ranking_teams import rank_team_all, ranking_teams, sort_win_data
from simulator.run_season_simulation import run_simulation, initialize_playoff


class TestRatingMachine(TestCase):
    def test_rating(self):
        self.assertTrue(SinglePlayerRating('201166'))  # Aaron Brooks
        self.assertTrue(SinglePlayerRating('201935'))  # James Harden
        self.assertTrue(SinglePlayerRating('201142'))  # Kevin Durant
        self.assertTrue(SinglePlayerRating('204001'))
        self.assertTrue(SinglePlayerRating('201566'))  # Russell Westbrook
        self.assertTrue(SinglePlayerRating('203112'))


class TestRunSeasonSimulation(TestCase):
    def test_run_simulation(self):
        simulation = run_simulation()
        print(simulation[0])
        print(simulation[1])
        print(simulation[2])
        self.assertTrue(simulation[0])
        self.assertTrue(simulation[1])
        self.assertTrue(simulation[2])
        self.assertEqual(simulation[3], 1230)
        self.assertTrue(max(simulation[1].values()) > 50)
        self.assertTrue(max(simulation[2].values()) > 40)


class TestOneGameSimulation(TestCase):
    """
    ATL player rating: 33
    BKN player rating: 87
    Apr 02, 2017: BKN, H = 91  ATL = 82
    Jan 10, 2017: BKN, H = 97  ATL = 117
    Mar 26, 2017: BKN, A = 107 ATL = 92
    Mar 08, 2017: BKN, A = 105 ATL = 110
    """

    def test_run_simulation(self):
        simulator = GameSimulation('1610612751', '1610612737')  # BKN vs ATL
        simulator2 = GameSimulation('1610612761', '1610612737')  # TOR vs ATL
        simulator3 = GameSimulation('1610612744', '1610612737')  # GSW vs ATL
        simulator4 = GameSimulation('1610612748', '1610612754')
        self.assertTrue(simulator.get_winner())
        self.assertTrue(simulator2.get_winner())
        self.assertTrue(simulator3.get_winner())
        self.assertEqual((simulator.get_team_one_score(), simulator.get_team_two_score()), (10, 7))
        self.assertTrue(simulator4.get_winner())

    def test_point_difference(self):
        simulator = GameSimulation('1610612751', '1610612737')
        self.assertEqual(simulator.point_difference(), (3, 4))


class TestRunSesasonSimulation(TestCase):
    def test_run_simulation(self):
        print(run_simulation())

    def test_initialize_playoff(self):
        print(initialize_playoff())


class TestRunPlayoffSimulation(TestCase):
    def test_run_single_series(self):
        print(run_single_series('1610612761', '1610612751'))  # TOR vs BKN
        print(run_single_series('1610612739', '1610612738'))  # CLE vs BOS
        print(run_single_series('1610612744', '1610612743'))  # GSW vs DEN
        print(run_single_series('1610612758', '1610612763'))  # SAS vs MEM

    def test_run_round_simulation(self):
        def helper_func(team1, team2):
            if team2 == '1610612743' or team1 == '1610612743':
                return [('1610612744', 3), ('1610612743', 4)]
            elif team1 == '1610612746' or team2 == '1610612746':
                return [('1610612746', 4), ('1610612762', 0)]
            elif team1 == '1610612745' or team2 == '1610612745':
                return [('1610612745', 4), ('1610612760', 1)]
            elif team1 == '1610612759' or team2 == '1610612759':
                return [('1610612759', 4), ('1610612763', 1)]
            elif team1 == '1610612761' or team2 == '1610612761':
                return [('1610612761', 4), ('1610612751', 0)]
            elif team1 == '1610612764' or team2 == '1610612764':
                return [('1610612764', 4), ('1610612754', 2)]
            elif team1 == '1610612748' or team2 == '1610612748':
                return [('1610612748', 4), ('1610612749', 2)]
            elif team2 == '1610612738' or team1 == '1610612738':
                return [('1610612739', 1), ('1610612738', 4)]

        def help_func_two(team1, team2):
            if team1 == '1610612764' or team2 == '1610612764':
                return [('1610612761', 1), ('1610612764', 4)]
            elif team1 == '1610612738' or team2 == '1610612738':
                return [('1610612748', 1), ('1610612738', 4)]
            elif team1 == '1610612746' or team2 == '1610612746':
                return [('1610612743', 2), ('1610612746', 4)]
            elif team1 == '1610612745' or team2 == '1610612745':
                return [('1610612745', 4), ('1610612759', 2)]

        def help_func_three(team1, team2):
            if team1 == '1610612738' or team2 == '1610612738':
                return [('1610612764', 2), ('1610612738', 4)]
            elif team1 == '1610612746' or team2 == '1610612746':
                return [('1610612746', 4), ('1610612745', 0)]

        # round one tests
        teams = {'east': {1: 'TOR', 2: 'CLE', 3: 'MIA', 4: 'WAS', 5: 'IND', 6: 'MIL', 7: 'BOS', 8: 'BKN'},
                 'west': {1: 'GSW', 2: 'SAS', 3: 'HOU', 4: 'LAC', 5: 'UTA', 6: 'OKC', 7: 'MEM', 8: 'DEN'}}
        one_result_one = ([[('1610612761', 4), ('1610612751', 0)], [('1610612764', 4), ('1610612754', 2)]], [1, 4])
        one_result_two = ([[('1610612748', 4), ('1610612749', 2)], [('1610612739', 1), ('1610612738', 4)]], [3, 7])
        one_result_three = ([[('1610612744', 3), ('1610612743', 4)], [('1610612746', 4), ('1610612762', 0)]], [8, 4])
        one_result_four = ([[('1610612745', 4), ('1610612760', 1)], [('1610612759', 4), ('1610612763', 1)]], [3, 2])

        self.assertEqual(run_round_simulation(teams['east'], 1, helper_func, 0), one_result_one)
        self.assertEqual(run_round_simulation(teams['east'], 1, helper_func, 1), one_result_two)
        self.assertEqual(run_round_simulation(teams['west'], 1, helper_func, 0), one_result_three)
        self.assertEqual(run_round_simulation(teams['west'], 1, helper_func, 1), one_result_four)

        # round two tests
        teams = {'east': {1: 'TOR', 4: 'WAS', 3: 'MIA', 7: 'BOS'}, 'west': {8: 'DEN', 4: 'LAC', 3: 'HOU', 2: 'SAS'}}
        two_result_one = ([[('1610612761', 1), ('1610612764', 4)], [('1610612748', 1), ('1610612738', 4)]], [4, 7])
        two_result_two = ([[('1610612743', 2), ('1610612746', 4)], [('1610612745', 4), ('1610612759', 2)]], [4, 3])

        self.assertEqual(run_round_simulation(teams['east'], 2, help_func_two), two_result_one)
        self.assertEqual(run_round_simulation(teams['west'], 2, help_func_two), two_result_two)

        # round three tests
        teams = {'east': {4: 'WAS', 7: 'BOS'}, 'west': {4: 'LAC', 3: 'HOU'}}
        three_result_one = ([[('1610612764', 2), ('1610612738', 4)]], ['BOS'])
        three_result_two = ([[('1610612746', 4), ('1610612745', 0)]], ['LAC'])

        self.assertEqual(run_round_simulation(teams['east'], 3, help_func_three), three_result_one)
        self.assertEqual(run_round_simulation(teams['west'], 3, help_func_three), three_result_two)

    def test_run_whole_simulation(self):
        result = run_whole_simulation()
        print(result)
        self.assertTrue(result)

    def test_get_playoff_teams(self):
        self.assertTrue(get_playoff_teams())


class TestRankingTeams(TestCase):
    def test_rank_teams(self):
        actual_result = ranking_teams()
        self.assertTrue(actual_result)

    def test_sort_win_data(self):
        actual_result = sort_win_data()
        print("sort win data: " + str(actual_result))
        self.assertTrue(actual_result)

    def test_rank_team_all(self):
        actual_result = rank_team_all()
        print("rank team all: " + str(actual_result))
        self.assertTrue(actual_result)
