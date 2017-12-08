# general imports
import json
from os.path import join, expanduser
from nba_py import player, team

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


def create_division_list():
    """
    create a file for the division list
    """
    data = {"east": ["ATL", "BKN", "BOS", "CHA", "CHI", "CLE", "DET", "IND", "MIA", "MIL", "NYK", "ORL", "PHI", "TOR",
                     "WAS"],
            "west": ["DAL", "DEN", "GSW", "HOU", "LAC", "LAL", "MEM", "MIN", "NOP", "OKC", "PHX", "POR", "SAC", "SAS",
                     "UTA"]}

    with open(DIVISION_LIST_PATH, 'w') as division_file:
        json.dump(data, division_file)


def get_id_from_abb(team_abb):
    with open(TEAM_DICT_PATH) as team_dict_file:
        team_dict = dict(json.load(team_dict_file))

    for team_id, abb in team_dict.items():
        if team_abb == abb:
            return team_id

