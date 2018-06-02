"""
This module retrieve box score data of a game from stats.nba.com and store
the data in a JSON file
"""

# general import
from json import load, dump
from os.path import join, exists
from nba_py import game
from stats_files import files_main
from stats_files import create_other_files


def create_box_score_files():
    """
    Creates a file storing box score data of a game given the ID
    """
    # create preliminary files for players
    create_other_files.init()
    with open(files_main.TEAM_DICT_PATH, 'r') as team_dict_file:
        team_dict = load(team_dict_file)

    # create a list of game IDs using the team game log files
    game_id_list = []
    for team in team_dict.values():
        team_path = join(files_main.TEAM_BASE_PATH, team + '.json')
        with open(team_path, 'r') as game_log_path:
            data = load(game_log_path)

        for single_game in data['resultSets'][0]['rowSet']:
            game_id_list.append(single_game[1])

    # output a message to let the user know that the program is running
    print("Retrieving box score data and creating files ... Please wait.")

    # retrieve data using game IDs from the list and store them in a file
    for game_id in game_id_list:
        path = join(files_main.GAME_BASE_PATH, game_id + '.json')
        if not exists(path):
            print("Retrieving " + game_id + " data")
            box_score_data = game.Boxscore(game_id).json
            with open(path, 'w') as box_score_file:
                dump(box_score_data, box_score_file)
