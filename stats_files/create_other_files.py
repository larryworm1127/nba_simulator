"""
This module checks if the major data files exists or not, if the file does
not exist, it will run the appropriate function in order to create one
"""

# general imports
from stats_files import *
from os.path import exists
from os import makedirs


# helper functions
def player_dict():
    if not exists(PLAYER_DICT_PATH):
        create_player_dict()


def team_dict():
    if not exists(TEAM_DICT_PATH):
        create_team_dict()


def player_list():
    if not exists(PLAYER_LIST_PATH):
        create_player_list()


def team_list():
    if not exists(TEAM_LIST_PATH):
        create_team_list()


def division_list():
    if not exists(DIVISION_LIST_PATH):
        create_division_list()


def team_name_dict():
    if not exists(TEAM_NAME_DICT_PATH):
        create_team_name_dict()


def game_list():
    if not exists(GAME_LIST_PATH):
        create_game_list_files()


# directory check functions
def check_assets_dir():
    """
    This function checks if a directory exists. If not it will create one
    """
    if not exists(PLAYER_BASE_PATH):
        makedirs(PLAYER_BASE_PATH)

    if not exists(TEAM_BASE_PATH):
        makedirs(TEAM_BASE_PATH)

    if not exists(OTHER_BASE_PATH):
        makedirs(OTHER_BASE_PATH)

    if not exists(PLAYER_SEASON_PATH):
        makedirs(PLAYER_SEASON_PATH)

    if not exists(PLAYER_RATING_PATH):
        makedirs(PLAYER_RATING_PATH)

    if not exists(TEAM_PLAYOFF_PATH):
        makedirs(TEAM_PLAYOFF_PATH)

    if not exists(TEAM_SEASON_PATH):
        makedirs(TEAM_SEASON_PATH)

    if not exists(GAME_BASE_PATH):
        makedirs(GAME_BASE_PATH)

    if not exists(SIMULATE_RESULT_PATH):
        makedirs(SIMULATE_RESULT_PATH)


# init
def init():
    check_assets_dir()
    player_list()
    team_list()
    team_dict()
    player_dict()
    division_list()
    game_list()
