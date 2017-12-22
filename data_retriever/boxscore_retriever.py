"""
This module retrieve boxscore data of a game from stats.nba.com and store
the data in a json file
"""

# general import
import json
from os.path import join, exists
from nba_py import game
from data_retriever import Main
from data_retriever import file_check


def create_boxscore_files():
    """
    Creates a file storing boxscore data of a game given the ID
    """
    # create preliminary files for players
    file_check.init()
    with open(Main.TEAM_DICT_PATH, 'r') as team_dict_file:
        team_dict = json.load(team_dict_file)

    # create a list of game IDs using the team game log files
    game_id_list = []
    for team in team_dict.values():
        team_path = join(Main.TEAM_BASE_PATH, team + '.json')
        with open(team_path, 'r') as game_log_path:
            data = json.load(game_log_path)

        for index in range(len(data['resultSets'][0]['rowSet'])):
            game_id_list.append(data['resultSets'][0]['rowSet'][index][1])

    # output a message to let the user know that the program is running
    print("Retrieving boxscore data and creating files ... Please wait.")

    # retrieve data using game IDs from the list and store them in a file
    for game_id in game_id_list:
        path = join(Main.GAME_BASE_PATH, game_id + '.json')
        if not exists(path):
            print("Retrieving " + game_id + " data")
            boxscore_data = game.Boxscore(game_id).json
            with open(path, 'w') as boxscore_file:
                json.dump(boxscore_data, boxscore_file)
