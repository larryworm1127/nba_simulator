"""
This module contains functions that will retrieve various stats data relating
to NBA players
"""

# general import
from json import load, dump
from os.path import join, exists
from nba_py import player
from stats_files import PLAYER_DICT_PATH, PLAYER_BASE_PATH
from stats_files import create_other_files


# helper functions
def create_game_log_profile(player_id, player_dict):
    """Creates a file storing game logs of a player given the ID

    :param player_dict: self explanatory
    :param player_id: the ID of the player
    """
    new_path = join(PLAYER_BASE_PATH, player_dict[player_id] + '.json')
    if not exists(new_path):
        print(
            "Retrieving player game log data and creating files ... Please wait.")
        game_log = player.PlayerGameLogs(player_id).json
        with open(new_path, 'w') as player_file:
            dump(game_log, player_file)


def create_player_profile(player_id, player_dict):
    """Creates a file storing various player information such as season
    performances, etc

    :param player_dict: self explanatory
    :param player_id: the ID of the player
    """
    new_path = join(PLAYER_BASE_PATH,
                    'season_stats/' + player_dict[player_id] + '.json')
    if not exists(new_path):
        print(
            "Retrieving player season stats data and creating files ... Please wait.")
        season_stats = player.PlayerCareer(player_id).regular_season_totals()
        with open(new_path, 'w') as season_file:
            dump(season_stats, season_file)


def init():
    """Loop through every single player ID and create a file for game log and a
    file for his profile
    """
    # create preliminary files for players
    create_other_files.init()
    with open(PLAYER_DICT_PATH, 'r') as player_dict_file:
        player_dict = load(player_dict_file)

    for player_id in player_dict.keys():
        create_game_log_profile(player_id, player_dict)
        create_player_profile(player_id, player_dict)
