"""
This module creates player ratings and sort the ratings into the appropriate team files
"""

# general imports
from stats_files import files_main
from simulator import rate_player
from os.path import join, exists
import json


# main functions
def sort_player_into_team():
    """
    create directories and files and sort players into appropriate team folders
    """
    # retrieve preliminary data
    with open(files_main.PLAYER_DICT_PATH, 'r') as player_dict_file:
        player_dict = json.load(player_dict_file)

    # calculate the player ratings
    player_ratings = {}
    for player_id in player_dict.keys():
        rating = rate_player.SinglePlayerRating(player_id)
        player_ratings[player_dict[player_id]] = rating.get_rating()

    # create team folders if they don't exist
    with open(files_main.TEAM_DICT_PATH, 'r') as team_dict_file:
        team_dict = json.load(team_dict_file)

    for team_abb in team_dict.values():
        sorted_dir = join(files_main.PLAYER_RATING_PATH, team_abb + '.json')
        if not exists(sorted_dir):
            # sort player ratings into teams directories
            sorted_player_ratings = []
            for index in player_dict.keys():
                player_name = player_dict[index]
                player_path = join(files_main.PLAYER_SEASON_PATH, player_name + '.json')
                with open(player_path, 'r') as player_file:
                    file = json.load(player_file)

                # put all the player rating for the same team into a dictionary
                if file[-1]["TEAM_ABBREVIATION"] == team_abb and file[-1]["SEASON_ID"] != '2016-17':
                    sorted_player_ratings.append(player_ratings[player_name])

            # put each of the player dictionary inside the team dictionary into a single file
            with open(sorted_dir, 'w') as outfile:
                json.dump(sorted_player_ratings, outfile)

    return True  # used in test cases
