"""
This module creates data for standing pages
"""

from json import load
from os import listdir
from os.path import join

from constant import TEAM_DICT, TEAM_SEASON_PATH, SIM_RESULT_PATH
from simulator.rank_teams import rank_team_all
from stats_files import get_abb_from_name


# main functions
def create_standing_data(season):
    if season == '2017-18':
        result = create_simulated_wl_data()
        return result
    else:
        result = create_wl_data(season)
        return result


def rank_teams(season):
    team_list = TEAM_DICT.values()

    team_win_list = []
    for team_abb in team_list:
        with open(join(TEAM_SEASON_PATH, team_abb + '.json')) as data_file:
            data = load(data_file)['resultSets'][0]['rowSet']

        for row in data:
            if row[3] == season:
                team_win_list.append((team_abb, data[data.index(row)][5]))

    team_win_list.sort(key=lambda win: win[1], reverse=True)

    result = {}
    rank = 1
    for team in team_win_list:
        result[rank] = team[0]
        rank += 1

    return result


def create_wl_data(season):
    order = ['images/GSW.png', 'images/SAS.png', 'images/HOU.png',
             'images/BOS.png', 'images/CLE.png', 'images/LAC.png',
             'images/TOR.png', 'images/UTA.png', 'images/WAS.png',
             'images/OKC.png', 'images/ATL.png', 'images/MEM.png',
             'images/IND.png', 'images/MIL.png', 'images/CHI.png',
             'images/MIA.png', 'images/POR.png', 'images/DEN.png',
             'images/DET.png', 'images/CHA.png', 'images/NOP.png',
             'images/DAL.png', 'images/SAC.png', 'images/MIN.png',
             'images/NYK.png', 'images/ORL.png', 'images/PHI.png',
             'images/LAL.png', 'images/PHX.png', 'images/BKN.png']

    with open(join(TEAM_SEASON_PATH, 'ATL.json')) as data_file:
        parsed_json = load(data_file)

    result_sets = parsed_json['resultSets']

    rankings = rank_teams(season)
    data_list = get_data(season, rankings)

    data_headers = ['TEAM_CITY', 'TEAM_NAME', 'WINS', 'LOSSES']

    headers = ['Logo', 'Rank', 'Team City', 'Team Name', 'Wins', 'Losses']
    result_row = []
    single_row = []
    rank = 1
    for row in data_list:
        indexes = find_indexes(result_sets, data_headers)
        single_row.append(order[rank - 1])
        single_row.append(rank)
        for index in indexes:
            single_row.append(row[index])
        result_row.append(single_row)
        single_row = []
        rank += 1

    return headers, result_row


def find_indexes(result_sets, headers):
    indexes = []
    header_data = result_sets[0]['headers']

    for header in headers:
        indexes.append(header_data.index(header))

    return indexes


def get_data(season, ranking=None):
    all_team_lists = []
    if ranking is None:
        list_iter = listdir(TEAM_SEASON_PATH)
    else:
        list_iter = [team_abb + '.json' for team_abb in ranking.values()]

    for single_file in list_iter:
        with open(join(TEAM_SEASON_PATH, single_file)) as data_file:
            parsed_json = load(data_file)

        result_sets = parsed_json['resultSets'][0]['rowSet']
        for row in result_sets:
            if row[3] == season:
                all_team_lists.append(row)

    return all_team_lists


def create_simulated_wl_data():
    with open(join(SIM_RESULT_PATH, 'win_count.json')) as win_file:
        win_list = load(win_file)

    with open(join(SIM_RESULT_PATH, 'loss_count.json')) as loss_file:
        loss_list = load(loss_file)

    with open(join(TEAM_SEASON_PATH, 'ATL.json')) as data_file:
        parsed_json = load(data_file)

    result_sets = parsed_json['resultSets']
    rankings = rank_team_all()
    data = get_data('2017-18', rankings)
    data_heading = ['TEAM_CITY', 'TEAM_NAME']

    result_header = ['Rank', 'Team City', 'Team Name', 'Wins', 'Losses']
    result_row = []
    single_row = []
    rank = 1
    for row in data:
        heading_index = find_indexes(result_sets, data_heading)
        single_row.append(rank)
        for index in heading_index:
            single_row.append(row[index])

        team_abb = get_abb_from_name(row[2])
        single_row.append(win_list[team_abb])
        single_row.append(loss_list[team_abb])
        result_row.append(single_row)

        single_row = []
        rank += 1

    return result_header, result_row
