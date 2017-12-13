# general imports
from json import load
from os.path import join
from data_retriever import Main
from os import listdir


def create_team_data():
    headers = ['Rank', 'Team City', 'Team Name', 'W', 'L', 'PPG', 'FG%', '3P%', 'DREB', 'OREB', 'AST', 'TOV', 'STL', 'BLK',
               'PF']
    rows = []
    new_row = []
    rank = 1

    with open(join(Main.TEAM_SEASON_PATH, 'ATL.json')) as data_file:
        parsed_json = load(data_file)

    result_sets = parsed_json['resultSets']

    temp_list = get_data()
    sort_data(temp_list)

    for row in temp_list:
        indexes = find_indexes(result_sets)
        new_row.append(rank)
        for index in indexes:
            new_row.append(row[index])
        rows.append(new_row)
        new_row = []
        rank += 1

    return headers, rows


def find_indexes(result_sets):
    headers = ['TEAM_CITY', 'TEAM_NAME', 'WINS', 'LOSSES', 'PTS', 'FG_PCT', 'FG3_PCT', 'DREB', 'OREB', 'AST', 'TOV',
               'STL', 'BLK', 'PF']
    indexes = []
    for result in result_sets:
        for k, v in result.items():
            if k == 'headers':
                for header in headers:
                    indexes.append(v.index(header))

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
