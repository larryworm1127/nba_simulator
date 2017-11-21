import json
import math
import random

from enum import Enum
from os.path import join
from nba_py import player
from data_retriever import Main

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
    Position.GUARD: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    Position.FORWARD: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    Position.CENTER: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}


class RatingMachine:
    def __init__(self, player_id):
        self.player_rating = 0
        self.data = prepare_data(player_id)
        self.player_stat = self.data[0]
        self.position = self.data[1]

        self.rate()

    def __str__(self):
        result = ""
        result += str(self.player_stat) + '\n'
        result += str(self.player_rating)
        return result

    def get_rating(self):
        return self.player_rating

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
    """
    Prepare the data needed to be used to calculate player ratings

    :param player_id: the ID of a specific player
    :return: a list containing player stats and a string for player position
    """
    # prepare player dict data
    with open(Main.PLAYER_DICT_PATH, 'r') as player_dict_file:
        player_dict = dict(json.load(player_dict_file))

    # load the season stats for the player
    player_name = player_dict[player_id]
    player_stat = {}
    path = join(Main.PLAYER_SEASON_PATH, player_name + '.json')
    with open(path) as season_file:
        data = json.load(season_file)

    for stat in Stats:
        player_stat[str(stat.name)] = data[-1][str(stat.name)]

    # determine the position of the player
    #player_summary = player.PlayerSummary(player_id).info()
    #if player_summary[0]['POSITION'] == 'G':
    #    position = Position.GUARD
    #elif player_summary[0]['POSITION'] == 'C':
    #    position = Position.CENTER
    #else:
    #    position = Position.FORWARD
    position = random.choice([Position.FORWARD, Position.GUARD, Position.CENTER])

    return player_stat, position



