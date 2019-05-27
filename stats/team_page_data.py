"""
This module creates data sets that will be displayed onto the team regular
season game pages
"""

from json import load
from os.path import join
from re import search

from constant import MATCHUP_INDEX, DATE_INDEX
from constant import SIM_RESULT_PATH, TEAM_BASE_PATH, TEAM_DICT
from constant import TeamGameLogDataIndices as Indices


# main functions
def get_games(team_abb):
    """Creates the data set from the team game log stats.

    :param team_abb: the team abbreviation of the team
    :return: the data to be displayed on the web page
    """
    with open(join(TEAM_BASE_PATH, team_abb + '.json')) as data_file:
        game_log_data = load(data_file)

    other_teams = [item for item in TEAM_DICT.values()]
    other_teams.remove(team_abb)
    game_dict = {team: [] for team in other_teams}
    game_list = game_log_data['resultSets'][0]['rowSet']

    # Loop through every game
    for team in other_teams:
        for game in game_list:

            # only populate result dict if the <matchup> contains <team>
            data = {}
            matchup = game[MATCHUP_INDEX]
            if search(team, matchup):
                game_url = "/stats/box_score/?gameID=" + game[1]
                data['url'] = game_url
                data['HEADER'] = matchup + ' ---- ' + game[DATE_INDEX]
                data['TAB_HEADERS'] = [category.name for category in Indices]
                data['DISPLAY'] = [game[category.value] for category in Indices]
                game_dict[team].append(data)

    return game_dict


def get_simulated_games(team_abb):
    """Creates the data set for simulated games.

    :param team_abb: the team abbreviation of the team
    :return: the data to be displayed on the web page
    """
    with open(join(SIM_RESULT_PATH, team_abb + '.json')) as data_file:
        team_data = load(data_file)

    other_teams = [item for item in TEAM_DICT.values()]
    other_teams.remove(team_abb)
    game_dict = {}

    for team in other_teams:
        single_team = {}
        tab_headers = [f'Game {str(num + 1)}' for num in
                       range(len(team_data[team]))]
        panel_header = team_abb + ' vs. ' + team
        single_team['TAB_HEADERS'] = tab_headers
        single_team['DISPLAY'] = team_data[team]
        single_team['HEADER'] = panel_header
        game_dict[team] = single_team

    return game_dict
