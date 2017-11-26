from unittest import TestCase
from simulator import player_rating_machine as rating
from simulator import run_season_simulation
from simulator import one_game_simulation as sim
from simulator import run_playoff_simulation


class TestRatingMachine(TestCase):
    def test_rating(self):
        self.assertTrue(rating.RatingMachine('201166'))  # Aaron Brooks
        self.assertTrue(rating.RatingMachine('201935'))  # James Harden
        self.assertTrue(rating.RatingMachine('201142'))  # Kevin Durant
        self.assertTrue(rating.RatingMachine('204001'))  # Porzingis
        self.assertTrue(rating.RatingMachine('201566'))  # Russell Westbrook
        self.assertTrue(rating.RatingMachine('203112'))


class TestRunSeasonSimulation(TestCase):
    def test_run_simulation(self):
        simulation = run_season_simulation.run_simulation()
        print(simulation[0])
        print(simulation[1])
        print(simulation[2])
        self.assertTrue(simulation[0])
        self.assertTrue(simulation[1])
        self.assertTrue(simulation[2])
        self.assertEqual(simulation[3], 1230)
        self.assertTrue(max(simulation[1].values()) > 50)
        self.assertTrue(max(simulation[2].values()) > 40)


"""
ATL player rating: 33
BKN player rating: 87
Apr 02, 2017: BKN, H = 91  ATL = 82
Jan 10, 2017: BKN, H = 97  ATL = 117
Mar 26, 2017: BKN, A = 107 ATL = 92
Mar 08, 2017: BKN, A = 105 ATL = 110
"""


class TestOneGameSimulation(TestCase):
    def test_run_simulation(self):
        simulator = sim.TeamScoringMachine('1610612751', '1610612737')  # BKN vs ATL
        simulator2 = sim.TeamScoringMachine('1610612761', '1610612737')  # TOR vs ATL
        simulator3 = sim.TeamScoringMachine('1610612744', '1610612737')  # GSW vs ATL
        simulator4 = sim.TeamScoringMachine('1610612748', '1610612754')
        self.assertTrue(simulator.get_winner())
        self.assertTrue(simulator2.get_winner())
        self.assertTrue(simulator3.get_winner())
        self.assertEqual((simulator.get_team_one_score(), simulator.get_team_two_score()), (10, 7))
        self.assertTrue(simulator4.get_winner())

    def test_point_difference(self):
        simulator = sim.TeamScoringMachine('1610612751', '1610612737')
        self.assertEqual(simulator.point_difference(), (3, 4))


class TestRunPlayoffSimulation(TestCase):
    def test_run_single_series(self):
        print(run_playoff_simulation.run_single_series('1610612761', '1610612751'))  # TOR vs BKN
        print(run_playoff_simulation.run_single_series('1610612739', '1610612738'))  # CLE vs BOS
        print(run_playoff_simulation.run_single_series('1610612744', '1610612743'))  # GSW vs DEN
        print(run_playoff_simulation.run_single_series('1610612758', '1610612763'))  # SAS vs MEM

    def test_run_round_simulation(self):
        teams = {'east': {1: 'TOR', 2: 'CLE', 3: 'MIA', 4: 'WAS', 5: 'IND', 6: 'MIL', 7: 'BOS', 8: 'BKN'},
                 'west': {1: 'GSW', 2: 'SAS', 3: 'HOU', 4: 'LAC', 5: 'UTA', 6: 'OKC', 7: 'MEM', 8: 'DEN'}}
        print(run_playoff_simulation.run_round_simulation(teams['east'], 1, 0))
        print(run_playoff_simulation.run_round_simulation(teams['east'], 1, 1))
        print(run_playoff_simulation.run_round_simulation(teams['west'], 1, 0))
        print(run_playoff_simulation.run_round_simulation(teams['west'], 1, 1))

        teams = {'east': {1: 'TOR', 4: 'WAS', 3: 'MIA', 2: 'CLE'}, 'west': {1: 'GSW', 4: 'LAC', 3: 'HOU', 2: 'SAS'}}
        print(run_playoff_simulation.run_round_simulation(teams['east'], 2))
        print(run_playoff_simulation.run_round_simulation(teams['east'], 2))
        print(run_playoff_simulation.run_round_simulation(teams['west'], 2))
        print(run_playoff_simulation.run_round_simulation(teams['west'], 2))

    def test_run_whole_simulation(self):
        print(run_playoff_simulation.run_whole_simulation())

    def test_get_playoff_teams(self):
        print(run_playoff_simulation.get_playoff_teams())
