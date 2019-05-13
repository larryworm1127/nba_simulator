import os
import os.path

from constant import *

__all__ = ['get_id_from_abb', 'get_abb_from_name']


# Helper functions
def check_assets_dir() -> None:
    """This function checks if a directory exists. If not it will create one.
    """
    directories = [PLAYER_BASE_PATH, TEAM_BASE_PATH, PLAYER_SEASON_PATH,
                   PLAYER_RATING_PATH, TEAM_PLAYOFF_PATH, TEAM_SEASON_PATH,
                   GAME_BASE_PATH, SIM_RESULT_PATH]

    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)


def get_id_from_abb(team_abb: str) -> str:
    """This function return the team ID given a team abbreviation.

    :param team_abb: the team abbreviation
    :return: the team ID
    """
    for team_id, abb in TEAM_DICT.items():
        if team_abb == abb:
            return team_id


def get_abb_from_name(team_name: str) -> str:
    """This function return the team abbreviation given a team name.

    :param team_name: the name of the team
    :return: the team abbreviation
    """
    for team_abb, name in TEAM_NAME_DICT.items():
        if team_name == name[1]:
            return team_abb
