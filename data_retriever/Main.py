# general imports
from json import load, dump
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
TEAM_NAME_DICT_PATH = join(OTHER_BASE_PATH, 'team_name_dict.json')


# main functions
def create_player_list():
    """
    retrieve player list and put it in a json file
    """
    player_list = player.PlayerList().json
    with open(PLAYER_LIST_PATH, 'w') as player_list_file:
        dump(player_list, player_list_file)


def create_team_list():
    """
    retrieve team list and put it in a json file
    """
    team_list = team.TeamList().json
    with open(TEAM_LIST_PATH, 'w') as team_list_file:
        dump(team_list, team_list_file)


def create_player_dict():
    """
    create a dictionary storing player ID and his name
    """
    with open(PLAYER_LIST_PATH, 'r') as player_list_file:
        player_list = load(player_list_file)['resultSets'][0]['rowSet']
    player_dict = {player_list[num][0]: player_list[num][6] for num in range(len(player_list))}

    with open(PLAYER_DICT_PATH, 'w') as player_dict_file:
        dump(player_dict, player_dict_file)


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

    print(final_result)
    with open(TEAM_NAME_DICT_PATH, 'w') as outfile:
        dump(final_result, outfile)


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
