"""
This module contains functions that will retrieve various stats data relating
to NBA players
"""
import json
import os.path

from nba_py import player

from constant import PLAYER_BASE_PATH, PLAYER_DICT


# helper functions
def create_game_log_profile(player_id, player_dict):
    """Creates a file storing game logs of a player given the ID.

    :param player_dict: self explanatory
    :param player_id: the ID of the player
    """
    new_path = os.path.join(PLAYER_BASE_PATH, f'{player_dict[player_id]}.json')
    if not os.path.exists(new_path):
        print("Retrieving player game log ... Please wait.")
        game_log = player.PlayerGameLogs(player_id).json
        with open(new_path, 'w') as player_file:
            json.dump(game_log, player_file)


def create_player_profile(player_id: str, player_dict) -> None:
    """Creates a file storing various player information.

    :param player_dict: self explanatory
    :param player_id: the ID of the player
    """
    new_path = os.path.join(PLAYER_BASE_PATH,
                            f'season_stats/{player_dict[player_id]}.json')
    if not os.path.exists(new_path):
        print("Retrieving player season stats ... Please wait.")
        season_stats = player.PlayerCareer(player_id).regular_season_totals()
        with open(new_path, 'w') as season_file:
            json.dump(season_stats, season_file)


def init() -> None:
    """Loop through every single player ID and create a file for game log and a
    file for his profile
    """
    for player_id in PLAYER_DICT.keys():
        create_game_log_profile(player_id, PLAYER_DICT)
        create_player_profile(player_id, PLAYER_DICT)
