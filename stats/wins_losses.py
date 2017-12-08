# general imports
from json import load
from os.path import join
from data_retriever import Main
from os import listdir
from nba_simulator.settings import BASE_DIR

import os


def create_wl_data():
    headers = ['Logo','Rank','Team City','Team Name','Wins','Losses']

    rows = []
    new_row = []
    rank = 1
    logo_list = get_logos()

    with open(join(Main.TEAM_SEASON_PATH, 'ATL.json')) as data_file:
        parsed_json = load(data_file)

    result_sets = parsed_json['resultSets']

    temp_list = get_data()
    sort_data(temp_list)

    for row in temp_list:
        indexes = find_indexes(result_sets)
        new_row.append(rank)
        for i in range(len(indexes)):
            new_row.append(row[indexes[i]])
        rows.append(new_row)
        new_row = []
        rank += 1

    return headers, rows, logo_list


def find_indexes(result_sets):
    headers = ['TEAM_CITY', 'TEAM_NAME', 'WINS', 'LOSSES']
    indexes = []
    for result in result_sets:
        for k, v in result.items():
            if k == 'headers':
                for h in range(len(headers)):
                    indexes.append(v.index(headers[h]))
    return indexes


def get_data():
    all_team_lists = []
    for single_file in listdir(Main.TEAM_SEASON_PATH):
        with open(join(Main.TEAM_SEASON_PATH, single_file)) as data_file:
            parsed_json = load(data_file)

        result_sets = parsed_json['resultSets']
        for result in result_sets:
            for k, v in result.items():
                if k == 'rowSet':
                    for row in v:
                        if row[3] == "2016-17":
                            all_team_lists.append(row)

    return all_team_lists


def sort_data(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if (l[j])[5] < (l[j + 1])[5]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp


def get_logos():
    logo_list = []
    for each_logo in listdir(os.path.join(BASE_DIR,'static/images')):
        logo_list.append(each_logo)

    return logo_list
