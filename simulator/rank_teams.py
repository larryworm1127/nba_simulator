"""
This module contains functions that rank teams based on the number of wins and
losses they have.
"""
import json
import os.path
from typing import List, Tuple, Dict

from constant import DIVISION_LIST, SIM_RANKING_PATH, SIM_RESULT_PATH


def ranking_teams() -> Dict[str, Dict]:
    """
    Rank teams in different conferences based on their wins and losses

    :return: A dictionary where the key is the team rank and the value is the
    team abbreviation.
    """
    # initialize variables
    result = {'east': {}, 'west': {}}
    win_data_list = sort_win_data()
    east_counter = 1
    west_counter = 1

    # sort each team in the sorted win list into specific conference
    for item in win_data_list:
        team_abb = item[0]
        if team_abb in DIVISION_LIST['east']:
            result['east'][east_counter] = team_abb
            east_counter += 1
        else:
            result['west'][west_counter] = team_abb
            west_counter += 1

    # store the new data
    with open(SIM_RANKING_PATH, 'w') as ranking_file:
        json.dump(result, ranking_file)

    return result


def sort_win_data() -> List[Tuple[str, int]]:
    """A helper function that ranks all the teams no matter which conference
    they are in

    :return: A list containing tuples of (team abbreviation, number of wins)
    """
    # get data
    win_count_path = os.path.join(SIM_RESULT_PATH, 'win_count.json')
    with open(win_count_path) as win_count_file:
        win_data = dict(json.load(win_count_file))

    # sort the teams
    win_list = [(team_abb, num_win) for team_abb, num_win in win_data.items()]
    win_list.sort(key=lambda win: win[1], reverse=True)

    # return result
    return win_list


def rank_team_all() -> Dict[int, str]:
    """This function calls sort_win_data() and creates a list containing only
    the team abbreviation but not the number of wins.

    :return: A dictionary where the key is the team rank and the value is the
    team abbreviation
    """
    result = {}
    win_data_list = sort_win_data()
    for rank in range(30):
        result[rank + 1] = win_data_list[rank][0]

    return result
