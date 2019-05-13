"""
This module creates player ratings and sort the ratings into the appropriate
team files
"""
import os.path
import json

from simulator import rate_player
from constant import PLAYER_RATING_PATH
from constant import PLAYER_SEASON_PATH
from constant import TEAM_DICT
from constant import PLAYER_DICT


# Main functions
def sort_player_into_team():
    """Create directories and files and sort data into appropriate folders.
    """
    # calculate the player ratings
    player_ratings = {}
    for player_id in PLAYER_DICT.keys():
        rating = rate_player.SinglePlayerRating(player_id)
        player_ratings[PLAYER_DICT[player_id]] = rating.get_rating()

    for team_abb in TEAM_DICT.values():
        sorted_dir = os.path.join(PLAYER_RATING_PATH, f'{team_abb}.json')
        if not os.path.exists(sorted_dir):
            # sort player ratings into teams directories
            sorted_player_ratings = []
            for index in PLAYER_DICT.keys():
                player_name = PLAYER_DICT[index]
                player_path = os.path.join(PLAYER_SEASON_PATH,
                                           f'{player_name}.json')
                with open(player_path, 'r') as player_file:
                    file = json.load(player_file)

                # put all the player rating for the same team into a dictionary
                if file[-1]["TEAM_ABBREVIATION"] == team_abb and \
                        file[-1]["SEASON_ID"] != '2016-17':
                    sorted_player_ratings.append(player_ratings[player_name])

            with open(sorted_dir, 'w') as outfile:
                json.dump(sorted_player_ratings, outfile)

    return True  # used in test cases
