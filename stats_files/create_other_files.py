"""
This module checks if the major data files exists or not, if the file does
not exist, it will run the appropriate function in order to create one
"""

# general imports
from stats_files import files_main
from os.path import exists
from os import makedirs


# file check functions - these functions check if a file
# exists or not. They will create the file by calling the
# corresponding functions in files_main.py if the file does not exists
def player_dict():
    if not exists(files_main.PLAYER_DICT_PATH):
        files_main.create_player_dict()


def team_dict():
    if not exists(files_main.TEAM_DICT_PATH):
        files_main.create_team_dict()


def player_list():
    if not exists(files_main.PLAYER_LIST_PATH):
        files_main.create_player_list()


def team_list():
    if not exists(files_main.TEAM_LIST_PATH):
        files_main.create_team_list()


def division_list():
    if not exists(files_main.DIVISION_LIST_PATH):
        files_main.create_division_list()


def team_name_dict():
    if not exists(files_main.TEAM_NAME_DICT_PATH):
        files_main.create_team_name_dict()


def game_list():
    if not exists(files_main.GAME_LIST_PATH):
        files_main.create_game_list_files()


# directory check functions
def check_assets_dir():
    """
    This function checks if a directory exists. If not it will create one
    """
    if not exists(files_main.PLAYER_BASE_PATH):
        makedirs(files_main.PLAYER_BASE_PATH)

    if not exists(files_main.TEAM_BASE_PATH):
        makedirs(files_main.TEAM_BASE_PATH)

    if not exists(files_main.OTHER_BASE_PATH):
        makedirs(files_main.OTHER_BASE_PATH)

    if not exists(files_main.PLAYER_SEASON_PATH):
        makedirs(files_main.PLAYER_SEASON_PATH)

    if not exists(files_main.PLAYER_RATING_PATH):
        makedirs(files_main.PLAYER_RATING_PATH)

    if not exists(files_main.TEAM_PLAYOFF_PATH):
        makedirs(files_main.TEAM_PLAYOFF_PATH)

    if not exists(files_main.TEAM_SEASON_PATH):
        makedirs(files_main.TEAM_SEASON_PATH)

    if not exists(files_main.GAME_BASE_PATH):
        makedirs(files_main.GAME_BASE_PATH)

    if not exists(files_main.SIMULATE_RESULT_PATH):
        makedirs(files_main.SIMULATE_RESULT_PATH)


# init
def init():
    check_assets_dir()
    player_list()
    team_list()
    team_dict()
    player_dict()
    division_list()
    game_list()
