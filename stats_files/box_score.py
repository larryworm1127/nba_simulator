"""
This module retrieve box score data of a game from stats.nba.com and store
the data in a JSON file
"""

# general import
import json
import os.path

from nba_py import game

from constant import TEAM_BASE_PATH, GAME_BASE_PATH, TEAM_DICT


def create_box_score_files():
    """Creates a file storing box score data of a game given the ID
    """
    # create a list of game IDs using the team game log files
    game_id_list = []
    for team in TEAM_DICT.values():
        team_path = os.path.join(TEAM_BASE_PATH, team + '.json')
        with open(team_path, 'r') as game_log_path:
            data = json.load(game_log_path)

        for single_game in data['resultSets'][0]['rowSet']:
            game_id_list.append(single_game[1])

    # output a message to let the user know that the program is running
    print("Retrieving box score data and creating files ...")

    # retrieve data using game IDs from the list and store them in a file
    for game_id in game_id_list:
        path = os.path.join(GAME_BASE_PATH, game_id + '.json')
        if not os.path.exists(path):
            print("Retrieving " + game_id + " data")
            box_score_data = game.Boxscore(game_id).json
            with open(path, 'w') as box_score_file:
                json.dump(box_score_data, box_score_file)
