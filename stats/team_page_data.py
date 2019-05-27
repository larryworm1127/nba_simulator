"""
This module creates data sets that will be displayed onto the team regular
season game pages
"""

from json import load
from os.path import join

from constant import SIM_RESULT_PATH
from constant import TEAM_BASE_PATH
from constant import TEAM_DICT
from constant import TEAM_SEASON_PATH


# main functions
def get_team_from_abb(team_abb):
    """Find the corresponding team city and team name given a team abbreviation.

    :param team_abb: the team abbreviation of a team
    :return: a string containing the team city and team name
    """
    with open(join(TEAM_SEASON_PATH, team_abb + '.json')) as data_file:
        data = load(data_file)['resultSets'][0]['rowSet']

    team_city = data[-2][1]
    team_name = data[-2][2]

    result = team_city + ' ' + team_name
    return result


def get_other_teams(team_abb):
    """Compute all the other teams in the league given a team abbreviation.

    :param team_abb: the team abbreviation of a team
    :return: a list containing all teams in the league except the given one
    """
    team_list = list(TEAM_DICT.values())
    team_list.remove(team_abb)
    return team_list


def get_games(team_abb):
    """Creates the data set from the team game log stats.

    :param team_abb: the team abbreviation of the team
    :return: the data to be displayed on the web page
    """
    with open(join(TEAM_BASE_PATH, team_abb + '.json')) as data_file:
        game_log_data = load(data_file)

    other_teams = get_other_teams(team_abb)
    game_dict = {team: [] for team in other_teams}
    headers = game_log_data['resultSets'][0]['headers']
    game_list = game_log_data['resultSets'][0]['rowSet']

    for team in other_teams:
        for game in game_list:
            single_game = {}
            if game[3][-3:] == team:
                data_list = []
                for header in headers:
                    data_list.append(game[headers.index(header)])

                game_url = "/stats/box_score/?gameID=" + game[1]
                single_game['url'] = game_url
                single_game['HEADER'] = data_list[3] + ' ---- ' + data_list[2]
                data = data_cleanup(headers, data_list)
                single_game['TAB_HEADERS'] = data[1]
                single_game['DISPLAY'] = data[0]
                game_dict[team].append(single_game)

    return game_dict


def data_cleanup(header, data_list):
    """A helper function for removing unwanted elements in the table data

    :param data_list: the data list of the table
    :param header: the header list of the table
    :return: the shortened version of the header list
    """
    result_header = header.copy()
    result_list = data_list.copy()

    for _ in range(4):
        result_header.pop(0)
        result_list.pop(0)

    for _ in range(11):
        result_header.pop(3)
        result_list.pop(3)

    return result_list, result_header


def get_simulated_games(team_abb):
    """Creates the data set for simulated games.

    :param team_abb: the team abbreviation of the team
    :return: the data to be displayed on the web page
    """
    with open(join(SIM_RESULT_PATH, team_abb + '.json')) as data_file:
        team_data = load(data_file)

    other_teams = get_other_teams(team_abb)
    game_dict = {}

    for team in other_teams:
        single_team = {}
        tab_headers = ['Game ' + str(num + 1) for num in
                       range(len(team_data[team]))]
        panel_header = team_abb + ' vs. ' + team
        single_team['TAB_HEADERS'] = tab_headers
        single_team['DISPLAY'] = team_data[team]
        single_team['HEADER'] = panel_header
        game_dict[team] = single_team

    return game_dict
