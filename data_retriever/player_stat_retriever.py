# general import
import json
from os.path import join
from nba_py import player
from data_retriever import Main
from data_retriever import file_check

# create preliminary files for players
file_check.init()
with open(Main.PLAYER_DICT_PATH, 'r') as player_dict_file:
    player_dict = json.load(player_dict_file)


# helper functions
def create_game_log_profile(player_id):
    """
    Creates a file storing game logs of a player given the ID

    :param player_id: the ID of the player
    """
    print("Retrieving player game log data and creating files ... Please wait.")
    new_path = join(Main.PLAYER_BASE_PATH, player_dict[player_id] + '.json')
    game_log = player.PlayerGameLogs(player_id).json
    with open(new_path, 'w') as player_file:
        json.dump(game_log, player_file)


def create_player_profile(player_id):
    """
    Creates a file storing various player information such as season performances, etc

    :param player_id:
    """
    print("Retrieving player season stats data and creating files ... Please wait.")
    new_path = join(Main.PLAYER_BASE_PATH, 'season_stats/' + player_dict[player_id] + '.json')
    season_stats = player.PlayerCareer(player_id).regular_season_totals()
    with open(new_path, 'w') as season_file:
        json.dump(season_stats, season_file)


def init():
    """
    Loop through every single player ID and create a file for game log and a file for his profile
    """
    for player_id in player_dict.keys():
        create_game_log_profile(player_id)
        create_player_profile(player_id)

init()
