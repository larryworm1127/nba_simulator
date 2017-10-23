from unittest import TestCase
import simulator.one_game_simulation as simulation


class TestSimulation(TestCase):
    def test_run_simulation(self):
        simulator = simulation.TeamScoringMachine(1610612751, 1610612737)
        self.assertEqual((simulator.get_team_one_score(), simulator.get_team_two_score()), (6, 7))

    def test_point_difference(self):
        simulator = simulation.TeamScoringMachine(1610612751, 1610612737)
        self.assertEqual(simulator.point_difference(), (3, 4))


"""
Apr 02, 2017: BKN, H = 91  ATL = 82
Jan 10, 2017: BKN, H = 97  ATL = 117
Mar 26, 2017: BKN, A = 107 ATL = 92
Mar 08, 2017: BKN, A = 105 ATL = 110
"""