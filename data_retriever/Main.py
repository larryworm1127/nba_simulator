# general imports
import json
from os.path import join, expanduser
from nba_py import player, team
from simulator import player_rating_machine
from data_retriever import file_check

# constant for the software
BASE = expanduser('~')
ASSET_BASE = join(BASE, 'assets')
TEAM_BASE_PATH = join(ASSET_BASE, 'team_stats')
PLAYER_BASE_PATH = join(ASSET_BASE, 'player_stats')
OTHER_BASE_PATH = join(ASSET_BASE, 'other_files')
GAME_BASE_PATH = join(ASSET_BASE, 'game_stats')
PLAYER_DICT_PATH = join(OTHER_BASE_PATH, 'player_dict.json')
TEAM_DICT_PATH = join(OTHER_BASE_PATH, 'team_dict.json')
PLAYER_LIST_PATH = join(OTHER_BASE_PATH, 'player_list.json')
TEAM_LIST_PATH = join(OTHER_BASE_PATH, 'team_list.json')
SEASON_STAT_PATH = join(ASSET_BASE, 'player_stats', 'season_stats')
PLAYER_RATING_PATH = join(ASSET_BASE, 'player_ratings')
TEAM_PLAYOFF_PATH = join(TEAM_BASE_PATH, 'playoff_stats')
SIMULATE_RESULT_PATH = join(ASSET_BASE, 'simulated_results')
GAME_LIST_PATH = join(OTHER_BASE_PATH, 'game_list.json')
DIVISION_LIST_PATH = join(OTHER_BASE_PATH, 'division_list.json')
TEAM_SEASON_PATH = join(TEAM_BASE_PATH, 'season_stats')


# main functions
def create_player_list():
    """
    retrieve player list and put it in a json file
    """
    player_list = player.PlayerList().json
    with open(PLAYER_LIST_PATH, 'w') as player_list_file:
        json.dump(player_list, player_list_file)


def create_team_list():
    """
    retrieve team list and put it in a json file
    """
    team_list = team.TeamList().json
    with open(TEAM_LIST_PATH, 'w') as team_list_file:
        json.dump(team_list, team_list_file)


def create_player_dict():
    """
    create a dictionary storing player ID and his name
    """
    with open(PLAYER_LIST_PATH, 'r') as player_list_file:
        player_list = json.load(player_list_file)
    player_dict = {player_list['resultSets'][0]['rowSet'][num][0]: player_list['resultSets'][0]['rowSet'][num][6] for
                   num in range(len(player_list['resultSets'][0]['rowSet']))}

    with open(PLAYER_DICT_PATH, 'w') as player_dict_file:
        json.dump(player_dict, player_dict_file)


def create_team_dict():
    """
    create a dictionary storing team ID and its abbreviation
    """
    with open(TEAM_LIST_PATH, 'r') as team_list_file:
        team_list = json.load(team_list_file)

    team_dict = {team_list['resultSets'][0]['rowSet'][num][1]: team_list['resultSets'][0]['rowSet'][num][-1] for num in
                 range(30)}
    with open(TEAM_DICT_PATH, 'w') as team_dict_file:
        json.dump(team_dict, team_dict_file)


def sort_player_into_team():
    """
    create directories and files and sort players into appropriate team folders
    """
    # retrieve preliminary data
    with open(PLAYER_DICT_PATH, 'r') as player_dict_file:
        player_dict = json.load(player_dict_file)

    # calculate the player ratings
    player_ratings = {}
    print("Rating players ... Please wait.")
    for player_id in player_dict.keys():
        rating = player_rating_machine.RatingMachine(player_id)
        player_ratings[player_dict[player_id]] = rating.get_rating()

    # create team folders if they don't exist
    print("Sorting players and creating files ... Please wait.")
    with open(TEAM_DICT_PATH, 'r') as team_dict_file:
        team_dict = json.load(team_dict_file)

    for team_abb in team_dict.values():
        # sort player ratings into teams directories
        sorted_player_ratings = []
        for index in player_dict.keys():
            player_name = player_dict[index]
            player_path = join(SEASON_STAT_PATH, player_name + '.json')
            with open(player_path, 'r') as player_file:
                file = json.load(player_file)

            # put all the player rating for the same team into a dictionary
            if file[-1]["TEAM_ABBREVIATION"] == team_abb and file[-1]["SEASON_ID"] != '2016-17':
                sorted_player_ratings.append(player_ratings[player_name])

        # put each of the player dictionary inside the team dictionary into a single file
        sorted_dir = join(PLAYER_RATING_PATH, team_abb + '.json')
        with open(sorted_dir, 'w') as outfile:
            json.dump(sorted_player_ratings, outfile)

    print("Sorting complete.")
