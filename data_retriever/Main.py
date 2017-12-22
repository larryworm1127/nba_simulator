"""
The main module of the data retrieval functionality. It contains all the
paths to the data folders/files and all the functions for creating and retrieving
single file data.
"""

# general imports
from json import load, dump
from os.path import join, expanduser, exists

from datetime import date, timedelta
from nba_py import player, team, Scoreboard

# constant for the data paths
# asset base paths
BASE = expanduser('~')
ASSET_BASE = join(BASE, 'assets')

# other base paths
TEAM_BASE_PATH = join(ASSET_BASE, 'team_stats')
PLAYER_BASE_PATH = join(ASSET_BASE, 'player_stats')
OTHER_BASE_PATH = join(ASSET_BASE, 'other_files')
GAME_BASE_PATH = join(ASSET_BASE, 'game_stats')
PLAYER_RATING_PATH = join(ASSET_BASE, 'player_ratings')
SIMULATE_RESULT_PATH = join(ASSET_BASE, 'simulated_results')

# directory paths within base paths
TEAM_PLAYOFF_PATH = join(TEAM_BASE_PATH, 'playoff_stats')
PLAYER_SEASON_PATH = join(PLAYER_BASE_PATH, 'season_stats')
TEAM_SEASON_PATH = join(TEAM_BASE_PATH, 'season_stats')
TEAM_DICT_PATH = join(OTHER_BASE_PATH, 'team_dict.json')

# file paths
PLAYER_DICT_PATH = join(OTHER_BASE_PATH, 'player_dict.json')
PLAYER_LIST_PATH = join(OTHER_BASE_PATH, 'player_list.json')
TEAM_LIST_PATH = join(OTHER_BASE_PATH, 'team_list.json')
GAME_LIST_PATH = join(OTHER_BASE_PATH, 'game_list.json')
DIVISION_LIST_PATH = join(OTHER_BASE_PATH, 'division_list.json')
SIMULATE_RANKING_PATH = join(SIMULATE_RESULT_PATH, 'ranking.json')
SIMULATE_PLAYOFF_PATH = join(SIMULATE_RESULT_PATH, 'playoff_result.json')
TEAM_NAME_DICT_PATH = join(OTHER_BASE_PATH, 'team_name_dict.json')


# main functions
def create_player_list():
    """
    retrieve player list and put it in a json file
    """
    player_list = player.PlayerList().json
    with open(PLAYER_LIST_PATH, 'w') as player_list_file:
        dump(player_list, player_list_file)

    if exists(PLAYER_LIST_PATH):  # test case use only
        return True


def create_team_list():
    """
    retrieve team list and put it in a json file
    """
    team_list = team.TeamList().json
    with open(TEAM_LIST_PATH, 'w') as team_list_file:
        dump(team_list, team_list_file)

    if exists(TEAM_LIST_PATH):  # test case use only
        return True


def create_player_dict():
    """
    create a dictionary storing player ID and his name
    """
    with open(PLAYER_LIST_PATH, 'r') as player_list_file:
        player_list = load(player_list_file)['resultSets'][0]['rowSet']
    player_dict = {player_list[num][0]: player_list[num][6] for num in range(len(player_list))}

    with open(PLAYER_DICT_PATH, 'w') as player_dict_file:
        dump(player_dict, player_dict_file)

    if exists(PLAYER_DICT_PATH):  # test case use only
        return True


def create_team_dict():
    """
    create a dictionary storing team ID and its abbreviation
    """
    with open(TEAM_LIST_PATH, 'r') as team_list_file:
        team_list = load(team_list_file)['resultSets'][0]['rowSet']

    team_dict = {team_list[num][1]: team_list[num][-1] for num in
                 range(30)}
    with open(TEAM_DICT_PATH, 'w') as team_dict_file:
        dump(team_dict, team_dict_file)

    if exists(TEAM_DICT_PATH):  # test case use only
        return True


def create_division_list():
    """
    create a file for the division list
    """
    data = {"east": ["ATL", "BKN", "BOS", "CHA", "CHI", "CLE", "DET", "IND", "MIA", "MIL", "NYK", "ORL", "PHI", "TOR",
                     "WAS"],
            "west": ["DAL", "DEN", "GSW", "HOU", "LAC", "LAL", "MEM", "MIN", "NOP", "OKC", "PHX", "POR", "SAC", "SAS",
                     "UTA"]}

    with open(DIVISION_LIST_PATH, 'w') as division_file:
        dump(data, division_file)

    if exists(DIVISION_LIST_PATH):  # test case use only
        return True


def create_team_name_dict():
    """
    create a file containing dictionary where the key is the
    team abbreviation and the value is the team name
    """
    with open(TEAM_DICT_PATH) as team_dict_file:
        team_list = load(team_dict_file).values()

    final_result = {}
    for team_abb in team_list:
        with open(join(TEAM_SEASON_PATH, team_abb + '.json')) as data_file:
            data = load(data_file)['resultSets'][0]['rowSet'][-1]

        value = [data[1], data[2]]
        final_result[team_abb] = value

    with open(TEAM_NAME_DICT_PATH, 'w') as outfile:
        dump(final_result, outfile)

    if exists(TEAM_NAME_DICT_PATH):  # test case use only
        return True


def date_range(start, end):
    """
    A generate that yield a data given a range of dates

    :param start: the start of the time interval
    :param end: the end of the time interval
    """
    for n in range(int((end - start).days)):
        yield start + timedelta(n)


def create_game_list_files():
    """
    Create a game list file by reading through
    """
    print("Create game list files ...")
    start_date = date(2017, 10, 17)
    end_date = date(2018, 4, 12)

    date_list = []
    for single_date in date_range(start_date, end_date):
        date_list.append(str(single_date).split('-'))

    game_list = []

    for day in date_list:
        games = []
        score_board = Scoreboard(month=int(day[1]), day=int(day[2]), year=int(day[0])).game_header()

        for item in score_board:
            print(str(day) + ": " + str(item['HOME_TEAM_ID']) + ', ' + str(item['VISITOR_TEAM_ID']))
            if item['HOME_TEAM_ID']:
                games.append((item['HOME_TEAM_ID'], item['VISITOR_TEAM_ID']))

        if games:
            game_list.append(games)

    with open(GAME_LIST_PATH, 'w') as outfile:
        dump(game_list, outfile)


def get_id_from_abb(team_abb):
    with open(TEAM_DICT_PATH) as team_dict_file:
        team_dict = dict(load(team_dict_file))

    for team_id, abb in team_dict.items():
        if team_abb == abb:
            return team_id


def get_abb_from_name(team_name):
    with open(TEAM_NAME_DICT_PATH) as team_name_file:
        team_data = dict(load(team_name_file))

    for team_abb, name in team_data.items():
        if team_name == name[1]:
            return team_abb
