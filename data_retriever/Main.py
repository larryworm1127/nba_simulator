# general imports
import json
from os.path import join

from nba_py import player, team

from simulator import player_rating_machine

# constant for the software
TEAM_BASE_PATH = "C:/nba_simulator/assets/team_stats"
PLAYER_BASE_PATH = "C:/nba_simulator/assets/player_stats"
OTHER_BASE_PATH = "C:/nba_simulator/assets/other_files"
PLAYER_DICT_PATH = "C:/nba_simulator/assets/other_files/player_dict.json"
TEAM_DICT_PATH = "C:/nba_simulator/assets/other_files/team_dict.json"
PLAYER_LIST_PATH = "C:/nba_simulator/assets/other_files/player_list.json"
SEASON_STAT_PATH = "C:/nba_simulator/assets/player_stats/season_stats"


# main functions
def create_player_list():
    """
    create all the preliminary files for players
    """
    # retrieve player list and put it in a json file
    player_list = player.PlayerList(season='2016-17').json
    player_list_path = join(OTHER_BASE_PATH, 'player_list.json')
    with open(player_list_path, 'w') as player_list_file:
        json.dump(player_list, player_list_file)


def create_player_dict():
    """
    create a dictionary storing player ID and his name

    :return:
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

    :return the created dictionary
    """
    team_list = team.TeamList().info()
    team_dict = {team_list[num]['TEAM_ID']: team_list[num]['ABBREVIATION'] for num in range(30)}
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
    for player_id in player_dict.keys():
        rating = player_rating_machine.RatingMachine(player_id)
        player_ratings[player_dict[player_id]] = rating.get_rating()

    print(player_ratings)


"""
    # create team folders if they don't exist
    sorted_team_dict = {}
    for team_abb in range(1):
        # sort player ratings into teams directories
        sorted_player_dict = {}
        for index in range(len(player_dict.keys())):
            player_name = player_dict[index]
            print("Player name: " + player_name)
            player_path = join(SEASON_STAT_PATH + player_name + '.json')
            with open(player_path, 'r') as player_file:
                file = json.load(player_file)
                print(file)

            # put all the player rating for the same team into a dictionary
            if file["TEAM_ABBREVIATION"] == team_abb:
                sorted_player_dict[player_name] = player_ratings[player_name]

        # add the player dictionary into team dictionary
        sorted_team_dict[team_abb] = sorted_player_dict.copy()

        # put each of the player dictionary inside the team dictionary into a single file
        sorted_dir = join(PLAYER_BASE_PATH + '/player_rating', team_abb)
        with open(sorted_dir, 'w') as outfile:
            json.dump(sorted_team_dict, outfile)

    return "done"
"""
#sort_player_into_team()
