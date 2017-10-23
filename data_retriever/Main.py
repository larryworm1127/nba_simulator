# general imports
from nba_py import player, team
from os.path import join
import json
from simulator import player_rating_machine

# constant for the software
TEAM_BASE_PATH = "C:/nba_simulator/assets/team_stats/"
PLAYER_BASE_PATH = "C:/nba_simulator/assets/player_stats/"
OTHER_BASE_PATH = "C:/nba_simulator/assets/other_files"


# main functions
def create_player_preliminary_data():
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
    # create a dictionary where player IDs are the keys and player names are the values
    player_list_path = join(OTHER_BASE_PATH, 'player_list.json')
    with open(player_list_path, 'r') as player_list_file:
        player_list = json.load(player_list_file)
    players = {player_list['resultSets'][0]['rowSet'][num][0]: player_list['resultSets'][0]['rowSet'][num][6] for num
               in range(len(player_list['resultSets'][0]['rowSet']))}

    return players


def create_team_dict():
    """
    create a dictionary storing team ID and its abbreviation

    :return the created dictionary
    """
    # creates a dictionary where the keys are team IDs and values are team abbreviations
    team_list = team.TeamList().info()
    teams = {team_list[num]['TEAM_ID']: team_list[num]['ABBREVIATION'] for num in range(30)}

    return teams


player_dict = create_player_dict()
team_dict = create_team_dict()


def sort_player_into_team():
    """
    create directories and files and sort players into appropriate team folders
    """
    # calculate the player ratings
    player_ratings = {}
    for player_id in player_dict.keys():
        rating = player_rating_machine.RatingMachine(player_id)
        player_ratings[player_dict[player_id]] = rating.get_rating()

    # create team folders if they don't exist
    sorted_team_dict = {}
    for team_abb in range(1):
        # sort player ratings into teams directories
        sorted_player_dict = {}
        for index in range(len(player_dict.keys())):
            player_name = player_dict[index]
            player_path = join(PLAYER_BASE_PATH, 'season_stats/' + player_name + '.json')
            with open(player_path, 'r') as player_file:
                file = json.load(player_file)

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
