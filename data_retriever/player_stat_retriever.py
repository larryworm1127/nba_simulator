# general import
import json
from os.path import join, exists
from nba_py import player
import data_retriever.Main as Main

# create preliminary files for players
path = join(Main.OTHER_BASE_PATH, 'player_list.json')
if not exists(path):
    Main.create_player_preliminary_data()

Main.create_player_dict()


# helper functions
def create_game_log_profile(player_id):
    """
    Creates a file storing game logs of a player given the ID

    :param player_id: the ID of the player
    """
    new_path = join(Main.PLAYER_BASE_PATH, Main.player_dict[player_id] + '.json')
    game_log = player.PlayerGameLogs(player_id).json
    with open(new_path, 'w') as player_file:
        json.dump(game_log, player_file)


def create_player_profile(player_id):
    """
    Creates a file storing various player information such as season performances, etc

    :param player_id:
    """
    new_path = join(Main.PLAYER_BASE_PATH, 'season_stats/' + Main.player_dict[player_id] + '.json')
    season_stats = player.PlayerCareer(player_id).regular_season_totals()
    with open(new_path, 'w') as season_file:
        json.dump(season_stats, season_file)


def init():
    """
    Loop through every single player ID and create a file for game log and a file for his profile
    """
    for player_id in Main.player_dict.keys():
        create_game_log_profile(player_id)
        create_player_profile(player_id)

