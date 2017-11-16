from unittest import TestCase
from simulator import run_season_simulation


class TestRun_simulation(TestCase):
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
