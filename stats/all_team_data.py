"""
This module creates table data for all team statistic page
"""

# general imports
from typing import Dict, List
from json import load
from os.path import join
from os import listdir

from constant import TEAM_SEASON_PATH


# main functions
def create_team_data(sort: str) -> Dict[str, List]:
    """Creates and sorts data from files so that the web page can read them

    :param sort: the type of sorting the web page requested
    :return: the data to be displayed on the web page
    """
    with open(join(TEAM_SEASON_PATH, 'ATL.json')) as data_file:
        parsed_json = load(data_file)

    result_sets = parsed_json['resultSets']

    data = get_data()
    data_headers = ['TEAM_CITY', 'TEAM_NAME', 'WINS', 'LOSSES', 'PTS', 'FG_PCT',
                    'FG3_PCT', 'DREB', 'OREB', 'AST', 'TOV', 'STL', 'BLK', 'PF']

    result_row = []
    single_row = []
    for row in data:
        indexes = find_indexes(result_sets, data_headers)
        for index in indexes:
            single_row.append(row[index])
        result_row.append(single_row)
        single_row = []

    result_headers = ['Team City', 'Team Name', 'W', 'L', 'PPG', 'FG%', '3P%',
                      'DREB', 'OREB', 'AST', 'TOV', 'STL', 'BLK', 'PF']

    if sort is not None and sort in result_headers:
        result_row = sort_data_by_header(sort, result_row, result_headers)

    display_data = {'headers': result_headers, 'rows': result_row}

    return display_data


def find_indexes(result_sets: Dict[str, List], headers: List[str]) -> List[int]:
    """Find the index of a list of headers within the result sets.

    :param result_sets: the data set that contains all headers
    :param headers: the list of headers that will be used to find the indexes
    :return: a list of index for the given headers
    """
    index = []
    header_data = result_sets[0]['headers']

    for header in headers:
        index.append(header_data.index(header))

    return index


def get_data() -> List:
    """Create a list containing all the team season stats.

    :return: A list containing the data to be sorted and modified
    """
    all_team_lists = []
    for single_file in listdir(TEAM_SEASON_PATH):
        with open(join(TEAM_SEASON_PATH, single_file)) as data_file:
            parsed_json = load(data_file)

        data = parsed_json['resultSets'][0]['rowSet']
        for row in data:
            if row[3] == "2016-17":
                all_team_lists.append(row)

    return all_team_lists


def sort_data_by_header(header, result_rows, headers):
    """A helper function for sorting the display data.

    :param header: the category of stats that will be used for sorting
    :param result_rows: the current data
    :param headers: the list of headers
    :return:
    """
    tuple_data = [tuple(row) for row in result_rows]
    header_index = headers.index(header)

    reverse = True
    if header == 'Team City' or header == 'Team Name':
        reverse = False
    tuple_data.sort(key=lambda data: data[header_index], reverse=reverse)
    return [list(row) for row in tuple_data]
