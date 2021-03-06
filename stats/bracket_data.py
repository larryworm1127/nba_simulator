"""
This module reads from team playoff game log data and select
specific data from it and create data that can be understood by Bracket.js
"""

from json import load
from os import listdir
from os.path import join

from constant import CONF_LIST, TEAM_PLAYOFF_PATH, TEAM_SEASON_PATH

# constant
TEAM_MATCH_LIST = [[1, 8, 4, 5], [3, 6, 2, 7]]
TEAM_OPPONENT = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}


# create other variables and access data from files
class BracketData:
    def __init__(self):
        self.final_data = {'east': {'teams': [], 'results': [[], [], []]},
                           'west': {'teams': [], 'results': [[], [], []]},
                           'final': {'teams': [], 'results': [[]]}}
        self.playoff_dict = {'east': {}, 'west': {}}
        self.conf_final_teams = {'east': [], 'west': []}

        teams = [file.split('.')[0] for file in listdir(TEAM_PLAYOFF_PATH)]

        div_list = {}
        for name in teams:
            with open(join(TEAM_SEASON_PATH, f"{name}.json")) as f:
                data = load(f)['resultSets'][0]['rowSet']
                division = 'east' if name in CONF_LIST['east'] else 'west'
                div_list[name] = division

            self.playoff_dict[division][data[-2][8]] = name

    def set_final_data(self, new_data):
        self.final_data = new_data.copy()

    # format first round data
    def format_data(self, division, index):
        team_check_list = TEAM_MATCH_LIST[index].copy()
        next_round_teams = []
        for team in TEAM_MATCH_LIST[index]:
            team_abb = self.playoff_dict[division][team]

            with open(join(TEAM_PLAYOFF_PATH, team_abb + '.json')) as f:
                team_data = load(f)['resultSets'][0]['rowSet']

            opponent = self.playoff_dict[division][TEAM_OPPONENT[team]]
            team_check_list.remove(TEAM_OPPONENT[team])
            if team in team_check_list:
                self.final_data[division]['teams'].append([team_abb, opponent])

                team_points = 0
                opponent_points = 0
                for index in range(len(team_data) - 1, -1, -1):
                    if team_data[index][3][-3:] == opponent:
                        if team_data[index][4] == 'W':
                            team_points += 1
                        else:
                            opponent_points += 1

                self.final_data[division]['results'][0].append(
                    [team_points, opponent_points])

                if team_points > opponent_points:
                    next_round_teams.append(team_abb)
                else:
                    next_round_teams.append(opponent)

        next_round_team = self.second_third_round_data(next_round_teams,
                                                       division, 2)
        self.conf_final_teams[division].append(next_round_team)

    # format second and third round data
    def second_third_round_data(self, team_list, division, round_num):
        team_abb = team_list[0]
        opponent = team_list[1]

        with open(join(TEAM_PLAYOFF_PATH, team_abb + '.json')) as playoff_file:
            team_data = load(playoff_file)['resultSets'][0]['rowSet']

        if division == 'final':
            self.final_data[division]['teams'].append([team_abb, opponent])

        team_points = 0
        opponent_points = 0
        for index in range(len(team_data) - 1, -1, -1):
            if team_data[index][3][-3:] == opponent:
                if team_data[index][4] == 'W':
                    team_points += 1
                else:
                    opponent_points += 1

        self.final_data[division]['results'][round_num - 1].append(
            [team_points, opponent_points])
        return team_abb if team_points > opponent_points else opponent

    def create_playoff_data(self):
        for div in ['east', 'west']:
            for idx in range(2):
                self.format_data(div, idx)

        final_teams = []
        for div in ['east', 'west']:
            final_team = self.second_third_round_data(
                self.conf_final_teams[div], div, 3)
            final_teams.append(final_team)

        self.second_third_round_data(final_teams, 'final', 1)
