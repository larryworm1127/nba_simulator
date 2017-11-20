# general import
import json
from os.path import join
from nba_py import game
from data_retriever import Main
from data_retriever import file_check

# create preliminary files for players
file_check.init()
with open(Main.TEAM_DICT_PATH, 'r') as team_dict_file:
    team_dict = json.load(team_dict_file)


# helper functions
def create_game_log_profile():
    """
    Creates a file storing boxscore data of a game given the ID
    """
    game_id_list = []
    for team in team_dict.values():
        team_path = join(Main.TEAM_BASE_PATH, team + '.json')
        with open(team_path, 'r') as game_log_path:
            data = json.load(game_log_path)
a
        for index in range(len(data['resultSets'][0]['rowSet'])):
            game_id_list.append(data['resultSets'][0]['rowSet'][index][1])

    print(game_id_list)
    print("Retrieving boxscore data and creating files ... Please wait.")
    for game_id in range(len(game_id_list)):
        print("Retrieving " + game_id_list[game_id] + " data")
        boxscore_data = game.Boxscore(game_id_list[game_id]).json
        path = join(Main.GAME_BASE_PATH, game_id_list[game_id] + '.json')
        with open(path, 'w') as boxscore_file:
            json.dump(boxscore_data, boxscore_file)


create_game_log_profile()