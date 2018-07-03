"""
This module simulate a single NBA games given two teams
"""

# general import
from json import load
import random
from os.path import join

from stats_files import TEAM_DICT_PATH, TEAM_BASE_PATH, PLAYER_RATING_PATH


class GameSimulation:
    """
    This class will rate two teams and give each of them a score. A winner
    will be determined using random but the chance of winning will be affected
    by the score difference between the two teams
    """
    def __init__(self, team_one_id, team_two_id):
        # create variables
        self.team_one = team_one_id
        self.team_two = team_two_id
        self.home_games = {1: [], 2: []}
        self.away_games = {1: [], 2: []}
        self.team1_games = []
        self.team2_games = []
        self.team1_score = 0
        self.team2_score = 0
        self.team1_ratings = {}
        self.team2_ratings = {}
        self.winner = None

        # set up team dict data
        with open(TEAM_DICT_PATH, 'r') as team_dict_file:
            self.team_dict = load(team_dict_file)

        # prepare data for simulation
        self.prepare_game_log_data()
        self.prepare_player_rating_data()

        # run simulation
        self.run_simulation()

    def __str__(self):
        result = ''
        result += "Home games: " + str(self.home_games) + '\n'
        result += "Away games: " + str(self.away_games) + '\n'
        result += "Team 1 games: " + str(self.team1_games) + '\n'
        result += "Team 2 games: " + str(self.team1_games) + '\n'
        result += "Team 1 score: " + str(self.team1_score) + '\n'
        result += "Team 2 score: " + str(self.team2_score) + '\n'
        result += "Winner: " + str(self.winner)
        return result

    def get_team_one_score(self):
        return self.team1_score

    def get_team_two_score(self):
        return self.team2_score

    def get_winner(self):
        return self.winner

    def prepare_game_log_data(self):
        # initialize data files
        team1_path = join(TEAM_BASE_PATH, self.team_dict[self.team_one] + '.json')
        team2_path = join(TEAM_BASE_PATH, self.team_dict[self.team_two] + '.json')
        with open(team1_path, 'r') as team1_file:
            data1 = load(team1_file)['resultSets'][0]['rowSet']
        with open(team2_path, 'r') as team2_file:
            data2 = load(team2_file)['resultSets'][0]['rowSet']

        # run a loop 82 times (82 games in a season for a single team)
        for num in range(82):
            # determine the two teams
            data1_teams = [data1[num][3][:3], data1[num][3][-3:], data1[num][3][4:-4]]
            data2_teams = [data2[num][3][:3], data2[num][3][-3:], data2[num][3][4:-4]]

            # find the corresponding game results and add them to either home game list
            # or away game list depending on the result of the condition
            if data1_teams[0] == self.team_dict[self.team_one] and data1_teams[1] == self.team_dict[self.team_two]:
                self.team1_games.append(data1[num])
                if data1_teams[2] == 'vs.':
                    self.home_games[1].append(data1[num])
                else:
                    self.away_games[1].append(data1[num])

            # do the same for team 2
            if data2_teams[0] == self.team_dict[self.team_two] and data2_teams[1] == self.team_dict[self.team_one]:
                self.team2_games.append(data2[num])
                if data2_teams[2] == 'vs.':
                    self.home_games[2].append(data2[num])
                else:
                    self.away_games[2].append(data2[num])

    def prepare_player_rating_data(self):
        # load files and put data in global variables
        team1_abb = self.team_dict[self.team_one]
        team2_abb = self.team_dict[self.team_two]
        team1_path = join(PLAYER_RATING_PATH, team1_abb + '.json')
        team2_path = join(PLAYER_RATING_PATH, team2_abb + '.json')
        with open(team1_path, 'r') as team1_file:
            self.team1_ratings = load(team1_file)

        with open(team2_path, 'r') as team2_file:
            self.team2_ratings = load(team2_file)

    def team_match_up(self):
        """
        Scores the two teams based on their match up from last season

        :return: a tuple containing the score for team 1 and team 2
        """
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
        """
        Scores the two teams based on how many points a team won against the other

        :return: a tuple containing the scores for both teams
        """
        score1 = 0
        score2 = 0

        # iterate through every single games played between the two teams
        num_iter = (len(self.team1_games))
        for game in range(num_iter):
            team_one_points = self.team1_games[game][-1]
            team_two_points = 0
            for num in range(len(self.team2_games)):
                if self.team1_games[num][2] == self.team2_games[game][2]:
                    team_two_points = self.team2_games[num][-1]
                    break

            # call helper function to score the teams after getting the points each team scored
            scores = point_difference_scoring_machine(team_one_points, team_two_points)
            score1 += scores[0]
            score2 += scores[1]

        return score1, score2

    def player_rating(self):
        """
        Scores the teams based on the rating of the players in the team

        :return: a tuple containing scores for both teams
        """
        team1_total = sum([rating for rating in self.team1_ratings])
        team2_total = sum([rating for rating in self.team2_ratings])
        difference = point_difference_scoring_machine(team1_total, team2_total)
        score1 = difference[0]
        score2 = difference[1]

        return score1, score2

    def run_simulation(self):
        """
        Run the single game simulation by calling all the scoring team functions
        and determine the winner through different random factors
        """
        # initialize variables by calling the scoring functions
        team_match_up = self.team_match_up()
        point_difference = self.point_difference()
        player_rating = self.player_rating()
        self.team1_score += team_match_up[0] + point_difference[0] + player_rating[0]
        self.team2_score += team_match_up[1] + point_difference[1] + player_rating[1]

        # calculate the difference between the scores and adjust the random factor
        difference = abs(self.team1_score - self.team2_score)
        random_num = random.randint(0, 10)

        # determine the winner using random
        if self.team2_score < self.team1_score:
            if difference <= 5:
                if random_num <= 5 + 1:
                    self.winner = self.team_one
                else:
                    self.winner = self.team_two
            elif 5 < difference <= 10:
                if random_num <= 5 + 2:
                    self.winner = self.team_one
                else:
                    self.winner = self.team_two
            elif 10 < difference <= 15:
                if random_num <= 5 + 3:
                    self.winner = self.team_one
                else:
                    self.winner = self.team_two
            else:
                if random_num <= 5 + 4:
                    self.winner = self.team_one
                else:
                    self.winner = self.team_two

        elif self.team1_score < self.team2_score:
            if difference <= 5:
                if random_num <= 5 + 1:
                    self.winner = self.team_two
                else:
                    self.winner = self.team_one
            elif 5 < difference <= 10:
                if random_num <= 5 + 2:
                    self.winner = self.team_two
                else:
                    self.winner = self.team_one
            elif 10 < difference <= 15:
                if random_num <= 5 + 3:
                    self.winner = self.team_two
                else:
                    self.winner = self.team_one
            else:
                if random_num <= 5 + 4:
                    self.winner = self.team_two
                else:
                    self.winner = self.team_one
        else:
            if random_num <= 5:
                self.winner = self.team_one
            else:
                self.winner = self.team_two


def point_difference_scoring_machine(team_one_points, team_two_points):
    """
    A helper function for scoring points for teams based on their
    points secondary points rated through their points per game

    :param team_one_points: the points team one scored through its point per game
    :param team_two_points: the points team two scored through its point per game
    :return: a tuple containing the score of the two teams
    """
    # calculate the difference between the points both team have
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

    if team_one_points == team_two_points:
        return 1, 1
