# general import
from nba_py import player
from os.path import join
import json
import nba_simulator.Constants as Constants

# retrieve player list and put it in a json file
players = player.PlayerList(season='2016-17').json
path = join(Constants.PLAYER_BASE_PATH, 'player_list.json')
with open(path, 'w') as outfile:
    json.dump(players, outfile)


# helper functions
def create_game_log_profile(player_id):
    new_path = join(Constants.PLAYER_BASE_PATH, Constants.PLAYER_DICT[player_id] + '.json')
    game_log = player.PlayerGameLogs(player_id).json
    with open(new_path, 'w') as player_file:
        json.dump(game_log, player_file)


def create_player_profile(player_id):
    new_path = join(Constants.PLAYER_BASE_PATH, 'season_stats/' + Constants.PLAYER_DICT[player_id] + '.json')
    season_stats = player.PlayerCareer(player_id).regular_season_totals()
    with open(new_path, 'w') as season_file:
        json.dump(season_stats, season_file)


def init():
    """
    Loop through every single team ID and create a file
    """
    for player_id in Constants.PLAYER_DICT.keys():
        create_game_log_profile(player_id)
        create_player_profile(player_id)

init()
