"""
This module checks if the major data files exists or not, if the file does
not exist, it will run the appropriate function in order to create one
"""

# general imports
from data_retriever import Main
from os.path import exists
from os import makedirs


# file check functions
def player_dict():
    if not exists(Main.PLAYER_DICT_PATH):
        Main.create_player_dict()


def team_dict():
    if not exists(Main.TEAM_DICT_PATH):
        Main.create_team_dict()


def player_list():
    if not exists(Main.PLAYER_LIST_PATH):
        Main.create_player_list()


def team_list():
    if not exists(Main.TEAM_LIST_PATH):
        Main.create_team_list()


def division_list():
    if not exists(Main.DIVISION_LIST_PATH):
        Main.create_division_list()


def team_name_dict():
    if not exists(Main.TEAM_NAME_DICT_PATH):
        Main.create_team_name_dict()


def game_list():
    if not exists(Main.GAME_LIST_PATH):
        Main.create_game_list_files()


# directory check functions
def check_assets_dir():
    if not exists(Main.PLAYER_BASE_PATH):
        makedirs(Main.PLAYER_BASE_PATH)

    if not exists(Main.TEAM_BASE_PATH):
        makedirs(Main.TEAM_BASE_PATH)

    if not exists(Main.OTHER_BASE_PATH):
        makedirs(Main.OTHER_BASE_PATH)

    if not exists(Main.PLAYER_SEASON_PATH):
        makedirs(Main.PLAYER_SEASON_PATH)

    if not exists(Main.PLAYER_RATING_PATH):
        makedirs(Main.PLAYER_RATING_PATH)

    if not exists(Main.TEAM_PLAYOFF_PATH):
        makedirs(Main.TEAM_PLAYOFF_PATH)

    if not exists(Main.TEAM_SEASON_PATH):
        makedirs(Main.TEAM_SEASON_PATH)

    if not exists(Main.GAME_BASE_PATH):
        makedirs(Main.GAME_BASE_PATH)

    if not exists(Main.SIMULATE_RESULT_PATH):
        makedirs(Main.SIMULATE_RESULT_PATH)


# init
def init():
    check_assets_dir()
    player_list()
    team_list()
    team_dict()
    player_dict()
    division_list()
    game_list()
    team_name_dict()
