import json
import nba_simulator.Constants as Constants
import math
from os.path import join
from enum import Enum

"""
Rating Mechanism

Points per game
Rebounds per game
Assists per game
Steals per game
Blocks per game
Turnover per game
Fouls per game
Field goal percentage per game
Free throw percentage per game
Minute per game
"""


class Position(Enum):
    GUARD = 1
    FORWARD = 2
    CENTER = 3


class Stats(Enum):
    PTS = 1
    REB = 2
    AST = 3
    STL = 4
    BLK = 5
    TOV = 6
    PF = 7
    FG_PCT = 8
    FT_PCT = 9
    MIN = 10


PLAYER_RATING = {
    Position.GUARD: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    Position.FORWARD: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    Position.CENTER: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}


class RatingMachine:
    def __init__(self, player_id):
        self.player_rating = 0
        self.player_dict = Constants.PLAYER_DICT
        self.player_stat = prepare_data(player_id)
        self.position = None

        self.rate()

    def __str__(self):
        result = ""
        result += str(self.player_stat) + '\n'
        result += str(self.player_rating)
        return result

    def rate(self):
        self.player_rating = math.ceil(self.points() + self.rebounds() + self.assists() + self.steals() +
                                       self.blocks() + self.turnover() + self.fouls() +
                                       self.field_goal_percentage() + self.free_throw_percentage())

    def points(self):
        result = self.player_stat['PTS'] * PLAYER_RATING[self.position][0]
        return result

    def rebounds(self):
        result = self.player_stat['REB'] * PLAYER_RATING[self.position][1]
        return result

    def assists(self):
        result = self.player_stat['AST'] * PLAYER_RATING[self.position][2]
        return result

    def steals(self):
        result = self.player_stat['STL'] * PLAYER_RATING[self.position][3]
        return result

    def blocks(self):
        result = self.player_stat['BLK'] * PLAYER_RATING[self.position][4]
        return result

    def turnover(self):
        result = self.player_stat['TOV'] * PLAYER_RATING[self.position][5]
        return result

    def fouls(self):
        result = self.player_stat['PF'] * PLAYER_RATING[self.position][6]
        return result

    def field_goal_percentage(self):
        result = self.player_stat['FG_PCT'] * PLAYER_RATING[self.position][7]
        return result

    def free_throw_percentage(self):
        result = self.player_stat['FT_PCT'] * PLAYER_RATING[self.position][8]
        return result

    def minutes(self):
        result = self.player_stat['MIN'] * PLAYER_RATING[self.position][9]
        return result


def prepare_data(player_id):
    player_name = Constants.PLAYER_DICT[player_id]
    player_stat = {}
    path = join(Constants.PLAYER_BASE_PATH + 'season_stats/', player_name + '.json')
    data = json.load(open(path))

    for stat in Stats:
        player_stat[str(stat.name)] = data[-1][str(stat.name)]

    return player_stat

print(RatingMachine(201166))  # Aaron Brooks
print(RatingMachine(201935))  # James Harden
print(RatingMachine(201142))  # Kevin Durant
print(RatingMachine(204001))  # Porzingis
print(RatingMachine(201566))  # Russell Westbrook
