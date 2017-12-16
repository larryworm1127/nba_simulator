# general imports
from json import load
from os.path import join
from data_retriever import Main
from os import listdir


def create_team_data():
    with open(join(Main.TEAM_SEASON_PATH, 'ATL.json')) as data_file:
        parsed_json = load(data_file)

    result_sets = parsed_json['resultSets']

    data = get_data()
    data_headers = ['TEAM_CITY', 'TEAM_NAME', 'WINS', 'LOSSES', 'PTS', 'FG_PCT', 'FG3_PCT', 'DREB', 'OREB', 'AST',
                    'TOV', 'STL', 'BLK', 'PF']

    result_row = []
    single_row = []
    for row in data:
        indexes = find_indexes(result_sets, data_headers)
        for index in indexes:
            single_row.append(row[index])
        result_row.append(single_row)
        single_row = []

    result_headers = ['Team City', 'Team Name', 'W', 'L', 'PPG', 'FG%', '3P%', 'DREB', 'OREB', 'AST', 'TOV', 'STL',
                      'BLK', 'PF']

    return result_headers, result_row


def find_indexes(result_sets, headers):
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

        data = parsed_json['resultSets'][0]['rowSet']
        for row in data:
            if row[3] == "2016-17":
                all_team_lists.append(row)
    return all_team_lists
