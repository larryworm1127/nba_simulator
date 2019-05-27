"""
This module creates table data for all team statistic page
"""

from json import load
from os import listdir
from os.path import join
from typing import Dict, List

from constant import TEAM_SEASON_PATH
from constant import TeamSeasonDataIndices as Indices


# main functions
def create_team_data(sort: str) -> Dict[str, List]:
    """Creates and sorts data from files so that the web page can read them

    :param sort: the type of sorting the web page requested
    :return: the data to be displayed on the web page
    """
    all_team_data = load_team_season_data()
    data_headers = [
        'TEAM_LOC', 'TEAM_NAME', 'WINS', 'LOSSES', 'PPG', 'FG_PCT', 'FG3_PCT',
        'DREB', 'OREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'PF'
    ]
    result_headers = [
        'Team City', 'Team Name', 'W', 'L', 'PPG', 'FG%', '3P%',
        'DREB', 'OREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'PF'
    ]

    reduced_data = [[row[Indices.__members__[header].value]
                     for header in data_headers] for row in all_team_data]

    # sort the data by the requested stats category
    if sort is not None and sort in result_headers:
        index = result_headers.index(sort)
        reverse = False if sort in ['Team City', 'Team Name'] else True
        reduced_data.sort(key=lambda data: data[index], reverse=reverse)

    display_data = {'headers': result_headers, 'rows': reduced_data}

    return display_data


def load_team_season_data() -> List:
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
