# general imports
from json import load
from os.path import join
from data_retriever import Main
from os import listdir
from simulator.ranking_teams import rank_team_all


def create_wl_data():
    headers = ['Logo', 'Rank', 'Team City', 'Team Name', 'Wins', 'Losses']
    rows = []
    new_row = []
    rank = 1
    order = ['images/GSW.png', 'images/SAS.png', 'images/HOU.png', 'images/BOS.png', 'images/CLE.png', 'images/LAC.png',
             'images/TOR.png', 'images/UTA.png', 'images/WAS.png', 'images/OKC.png', 'images/ATL.png', 'images/MEM.png',
             'images/IND.png', 'images/MIL.png', 'images/CHI.png', 'images/MIA.png', 'images/POR.png', 'images/DEN.png',
             'images/DET.png', 'images/CHA.png', 'images/NOP.png', 'images/DAL.png', 'images/SAC.png', 'images/MIN.png',
             'images/NYK.png', 'images/ORL.png', 'images/PHI.png', 'images/LAL.png', 'images/PHX.png', 'images/BKN.png']

    with open(join(Main.TEAM_SEASON_PATH, 'ATL.json')) as data_file:
        parsed_json = load(data_file)

    result_sets = parsed_json['resultSets']

    temp_list = get_data()
    sort_data(temp_list)

    for row in temp_list:
        indexes = find_indexes(result_sets)
        new_row.append(order[rank - 1])
        new_row.append(rank)
        for index in indexes:
            new_row.append(row[index])
        rows.append(new_row)
        new_row = []
        rank += 1

    return headers, rows


def find_indexes(result_sets):
    headers = ['TEAM_CITY', 'TEAM_NAME', 'WINS', 'LOSSES']
    indexes = []

    header_data = result_sets[0]['headers']

    for header in headers:
        indexes.append(header_data.index(header))

    return indexes


def get_data():
    all_team_lists = []
    for single_file in listdir(Main.TEAM_SEASON_PATH):
        with open(join(Main.TEAM_SEASON_PATH, single_file)) as data_file:
            parsed_json = load(data_file)

        result_sets = parsed_json['resultSets'][0]['rowSet']
        for row in result_sets:
            if row[3] == "2016-17":
                all_team_lists.append(row)

    return all_team_lists


def sort_data(lst):
    for i in range(len(lst) - 1, 0, -1):
        for index in range(i):
            if (lst[index])[5] < (lst[index + 1])[5]:
                temp = lst[index]
                lst[index] = lst[index + 1]
                lst[index + 1] = temp


def create_simulated_wl_data():
    with open(Main.SIMULATE_RESULT_PATH, 'win')
    rankings = rank_team_all()