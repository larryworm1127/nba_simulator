"""
This module creates player ratings based on their performances from last season
"""
import json
import math
import enum
import os.path
from typing import Dict

from constant import PLAYER_SEASON_PATH, PLAYER_DICT


# preliminary variables
class Stats(enum.Enum):
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
CATEGORIES = ['PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'FG_PCT',
              'FT_PCT', 'MIN']


class SinglePlayerRating:
    """Player Rating Class

    This class creates rating based on the player's various performances in
    different categories from the previous season.
    """
    player_rating: int
    player_stat: Dict

    def __init__(self, player_id: str) -> None:
        self.player_stat = prepare_data(player_id)
        self.player_rating = self.rate()

        self.rate()

    def __str__(self) -> str:
        result = ""
        result += str(self.player_stat) + '\n'
        result += str(self.player_rating)
        return result

    def get_rating(self) -> int:
        """Returns player rating.
        """
        return self.player_rating

    def rate(self) -> int:
        """By calling all the factor methods, a player rating is determined by
        adding all the return values from the factor methods
        """
        rating = 0
        for index, cat in enumerate(CATEGORIES):
            rating += self.player_stat[cat] * MULTIPLY_FACTOR[index]

        return math.ceil(rating)


def prepare_data(player_id: str) -> Dict:
    """Prepare the data needed to be used to calculate player ratings.

    :param player_id: the ID of a specific player
    :return: a list containing player stats and a string for player position
    """
    # load the season stats for the player
    player_name = PLAYER_DICT[player_id]
    player_stat = {}
    path = os.path.join(PLAYER_SEASON_PATH, player_name + '.json')
    with open(path) as season_file:
        data = json.load(season_file)

    for stat in Stats:
        player_stat[str(stat.name)] = data[-1][str(stat.name)]

    return player_stat
