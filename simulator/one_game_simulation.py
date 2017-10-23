# general import
import json
from os.path import join

import data_retriever.Main as Main

"""
Team match up histories:
    home game:
        win = +1
        loss = 0
    away game:
        win = +2
        loss = 0
Team match up average points per game
Team player ratings
Team match up average points differential
    between 0 and 10 = +1
    between 10 and 20 = +2
    between 20 and 30 = +3
    30+ = +4
"""


class TeamScoringMachine:
    def __init__(self, team_one_id, team_two_id):
        # create variables
        self.team_one = team_one_id
        self.team_two = team_two_id
        self.home_games = {1: [], 2: []}
        self.away_games = {1: [], 2: []}
        self.team_one_games = []
        self.team_two_games = []
        self.team_one_score = 0
        self.team_two_score = 0
        self.team_dict = Main.team_dict

        # prepare data for simulation
        self.prepare_data()

        # run simulation
        self.run_simulation()

    def __str__(self):
        result = ''
        result += "Home games: " + str(self.home_games) + '\n'
        result += "Away games: " + str(self.away_games) + '\n'
        result += "Team 1 games: " + str(self.team_one_games) + '\n'
        result += "Team 2 games: " + str(self.team_two_games) + '\n'
        result += "Team 1 score: " + str(self.team_one_score) + '\n'
        result += "Team 2 score: " + str(self.team_two_score)
        return result

    def get_team_one_score(self):
        return self.team_one_score

    def get_team_two_score(self):
        return self.team_two_score

    def prepare_data(self):
        path1 = join(Main.TEAM_BASE_PATH, self.team_dict[self.team_one] + '.json')
        path2 = join(Main.TEAM_BASE_PATH, self.team_dict[self.team_two] + '.json')
        with open(path1) as file1:
            data1 = json.load(file1)
        with open(path2) as file2:
            data2 = json.load(file2)

        for num in range(82):
            data1_teams = string_processor(data1['resultSets'][0]['rowSet'][num][3])
            data2_teams = string_processor(data2['resultSets'][0]['rowSet'][num][3])
            if data1_teams[0] == self.team_dict[self.team_one] and data1_teams[1] == self.team_dict[self.team_two]:
                self.team_one_games.append(data1['resultSets'][0]['rowSet'][num])
                if data1_teams[2] == 'vs.':
                    self.home_games[1].append(data1['resultSets'][0]['rowSet'][num])
                else:
                    self.away_games[1].append(data1['resultSets'][0]['rowSet'][num])

            if data2_teams[0] == self.team_dict[self.team_two] and data2_teams[1] == self.team_dict[self.team_one]:
                self.team_two_games.append(data2['resultSets'][0]['rowSet'][num])
                if data2_teams[2] == 'vs.':
                    self.home_games[2].append(data2['resultSets'][0]['rowSet'][num])
                else:
                    self.away_games[2].append(data2['resultSets'][0]['rowSet'][num])

    def team_match_up(self):
        score1 = 0
        score2 = 0

        for home_game in self.home_games[1]:
            if home_game[4] == 'W':
                score1 += 1
            elif home_game[4] == 'L':
                score2 += 1

        for away_game in self.away_games[1]:
            if away_game[4] == 'W':
                score1 += 2
            elif away_game[4] == 'L':
                score2 += 2

        return score1, score2

    def point_difference(self):
        score1 = 0
        score2 = 0

        num_iter = (len(self.team_one_games))
        for game in range(num_iter):
            team_one_points = self.team_one_games[game][-1]
            team_two_points = 0
            for num in range(len(self.team_two_games)):
                if self.team_two_games[num][2] == self.team_one_games[game][2]:
                    team_two_points = self.team_two_games[num][-1]
                    break

            scores = point_difference_scoring_machine(team_one_points, team_two_points)
            score1 += scores[0]
            score2 += scores[1]

        return score1, score2

    def run_simulation(self):
        team_match_up = self.team_match_up()
        point_difference = self.point_difference()
        self.team_one_score += team_match_up[0] + point_difference[0]
        self.team_two_score += team_match_up[1] + point_difference[1]


def string_processor(string):
    result = [string[:3], string[-3:], string[4:-4]]
    return result


def point_difference_scoring_machine(team_one_points, team_two_points):
    difference = abs(team_one_points - team_two_points)

    if team_one_points > team_two_points:
        if difference < 10:
            return 1, 0
        elif 20 > difference >= 10:
            return 2, 0
        elif 30 > difference >= 20:
            return 3, 0
        elif difference >= 30:
            return 4, 0

    if team_two_points > team_one_points:
        if difference < 10:
            return 0, 1
        elif 20 > difference >= 10:
            return 0, 2
        elif 30 > difference >= 20:
            return 0, 3
        elif difference >= 30:
            return 0, 4

