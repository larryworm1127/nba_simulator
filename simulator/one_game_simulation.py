# general import
from os.path import join
import json
import nba_simulator.Constants as Constants

"""
Team match up histories:
    home game:
        win = +1
        loss = 0
    away game:
        win = +2
        loss = 0
Team offensive and defensive ratings
    between 0 and 5 = +1
    between 5 and 10 = +2
    between 10 and 15 = +3
    between 15 and 20 = +4
    between 20 and 25 = +5
    25+ = +6
Team match up average points per game
Team player ratings
Team match up average points differential
    between 0 and 10 = +1
    between 10 and 20 = +2
    between 20 and 30 = +3
    30+ = +4
"""


class Simulation:
    def __init__(self, team_one_id, team_two_id):
        # create variables
        self.team_one = team_one_id
        self.team_two = team_two_id
        self.home_games = {1: [], 2: []}
        self.away_games = {1: [], 2: []}
        self.team_dict = Constants.TEAM_DICT
        self.team_one_score = 0
        self.team_two_score = 0

        # prepare data for simulation
        self.prepare_data()

        # run simulation
        self.run_simulation()

    def __str__(self):
        result = ''
        result += str(self.home_games) + '\n'
        result += str(self.away_games) + '\n'
        result += str(self.team_one_score) + '\n'
        result += str(self.team_two_score)
        return result

    def prepare_data(self):
        path1 = join(Constants.TEAM_BASE_PATH, self.team_dict[self.team_one] + '.json')
        path2 = join(Constants.TEAM_BASE_PATH, self.team_dict[self.team_two] + '.json')
        data1 = json.load(open(path1))
        data2 = json.load(open(path2))

        for num in range(82):
            data1_teams = string_processor(data1['resultSets'][0]['rowSet'][num][3])
            data2_teams = string_processor(data2['resultSets'][0]['rowSet'][num][3])
            if data1_teams[0] == self.team_dict[self.team_one] and data1_teams[1] == self.team_dict[self.team_two]:
                if data1_teams[2] == 'vs.':
                    self.home_games[1].append(data1['resultSets'][0]['rowSet'][num])
                else:
                    self.away_games[1].append(data1['resultSets'][0]['rowSet'][num])

            if data2_teams[0] == self.team_dict[self.team_two] and data2_teams[1] == self.team_dict[self.team_one]:
                if data2_teams[2] == 'vs.':
                    self.home_games[2].append(data2['resultSets'][0]['rowSet'][num])
                else:
                    self.away_games[2].append(data2['resultSets'][0]['rowSet'][num])

    def team_match_up(self):
        "return score"
        for home_game in self.home_games[1]:
            if home_game[4] == 'W':
                self.team_one_score += 1
            elif home_game[4] == 'L':
                self.team_two_score += 1

        for away_game in self.away_games[1]:
            if away_game[4] == 'W':
                self.team_one_score += 2
            elif away_game[4] == 'L':
                self.team_two_score += 2

    def point_differential(self):
        team_one_points = 0
        team_two_points = 0

        for t1_home in self.home_games[1]:
            team_one_points = t1_home[-1]
            for t2_away in self.away_games[2]:
                if t1_home[2] == t2_away[2]:
                    team_two_points = t2_away[-1]
                    break

        self.point_difference_scoring_machine(team_one_points, team_two_points)

        for t2_home in self.home_games[2]:
            team_one_points = t2_home[-1]
            for t1_away in self.away_games[1]:
                if t2_home[2] == t1_away[2]:
                    team_two_points = t1_away[-1]
                    break

        self.point_difference_scoring_machine(team_one_points, team_two_points)

    def point_difference_scoring_machine(self, team_one_points, team_two_points):
        difference = abs(team_one_points - team_two_points)

        if team_one_points > team_two_points:
            if difference < 10:
                self.team_one_score += 1
            elif 20 > difference >= 10:
                self.team_one_score += 2
            elif 30 > difference >= 20:
                self.team_one_score += 3
            elif difference >= 30:
                self.team_one_score += 4

        if team_two_points > team_one_points:
            if difference < 10:
                self.team_two_score += 1
            elif 20 > difference >= 10:
                self.team_two_score += 2
            elif 30 > difference >= 20:
                self.team_two_score += 3
            elif difference >= 30:
                self.team_two_score += 4

    def run_simulation(self):
        self.team_match_up()
        self.point_differential()


def string_processor(string):
    result = [string[:3], string[-3:], string[4:-4]]
    return result


print(Simulation(1610612751, 1610612737))
