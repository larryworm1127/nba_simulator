"""
This module creates player ratings based on their performances from last season
"""

# general imports
from json import load
from math import ceil
from enum import Enum
from os.path import join

from stats_files import Main


# preliminary variables
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


MULTIPLY_FACTOR = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


class SinglePlayerRating:
    """
    This class creates rating based on the player's various
    performances in different categories from the previous season
    """

    def __init__(self, player_id):
        self.player_rating = 0
        self.data = prepare_data(player_id)
        self.player_stat = self.data

        self.rate()

    def __str__(self):
        result = ""
        result += str(self.player_stat) + '\n'
        result += str(self.player_rating)
        return result

    def get_rating(self):
        return self.player_rating

    def rate(self):
        """
        By calling all the factor methods, a player rating is determined by adding all the
        return values from the factor methods
        """
        self.player_rating = ceil(self.points() + self.rebounds() + self.assists() + self.steals() +
                                  self.blocks() + self.turnover() + self.fouls() +
                                  self.field_goal_percentage() + self.free_throw_percentage())

    def points(self):
        result = self.player_stat['PTS'] * MULTIPLY_FACTOR[0]
        return result

    def rebounds(self):
        result = self.player_stat['REB'] * MULTIPLY_FACTOR[1]
        return result

    def assists(self):
        result = self.player_stat['AST'] * MULTIPLY_FACTOR[2]
        return result

    def steals(self):
        result = self.player_stat['STL'] * MULTIPLY_FACTOR[3]
        return result

    def blocks(self):
        result = self.player_stat['BLK'] * MULTIPLY_FACTOR[4]
        return result

    def turnover(self):
        result = self.player_stat['TOV'] * MULTIPLY_FACTOR[5]
        return result

    def fouls(self):
        result = self.player_stat['PF'] * MULTIPLY_FACTOR[6]
        return result

    def field_goal_percentage(self):
        result = self.player_stat['FG_PCT'] * MULTIPLY_FACTOR[7]
        return result

    def free_throw_percentage(self):
        result = self.player_stat['FT_PCT'] * MULTIPLY_FACTOR[8]
        return result

    def minutes(self):
        result = self.player_stat['MIN'] * MULTIPLY_FACTOR[9]
        return result


def prepare_data(player_id):
    """
    Prepare the data needed to be used to calculate player ratings

    :param player_id: the ID of a specific player
    :return: a list containing player stats and a string for player position
    """
    # prepare player dict data
    with open(Main.PLAYER_DICT_PATH, 'r') as player_dict_file:
        player_dict = dict(load(player_dict_file))

    # load the season stats for the player
    player_name = player_dict[player_id]
    player_stat = {}
    path = join(Main.PLAYER_SEASON_PATH, player_name + '.json')
    with open(path) as season_file:
        data = load(season_file)

    for stat in Stats:
        player_stat[str(stat.name)] = data[-1][str(stat.name)]

    return player_stat
