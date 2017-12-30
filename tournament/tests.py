from unittest import TestCase
from tournament.create_bracket_data import format_data, second_third_round_data, conf_final_teams, final_data


class TestFormat_data(TestCase):
    def test_format_data(self):
        for div in ['east', 'west']:
            for idx in range(2):
                format_data(div, idx)

        final_teams = []
        for div in ['east', 'west']:
            final_team = second_third_round_data(conf_final_teams[div], div, 3)
            final_teams.append(final_team)

        second_third_round_data(final_teams, 'final', 1)

        print(final_data)
        self.assertTrue(final_data)
