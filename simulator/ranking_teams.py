"""
This module contains functions that rank teams based on the number of wins and losses they have
"""

# general imports
import json
from data_retriever import Main
from os.path import join


def ranking_teams():
    """
    Rank teams in different conferences based on their wins and losses

    :return: A dictionary where the key is the team rank and the value is the team abbreviation
    """
    with open(Main.DIVISION_LIST_PATH) as division_list_file:
        division_list = json.load(division_list_file)

    result = {'east': {}, 'west': {}}
    win_data_list = sort_win_data()
    east_counter = 1
    west_counter = 1
    for item in win_data_list:
        team_abb = item[0]
        if team_abb in division_list['east']:
            result['east'][east_counter] = team_abb
            east_counter += 1
        else:
            result['west'][west_counter] = team_abb
            west_counter += 1

    with open(Main.SIMULATE_RANKING_PATH, 'w') as ranking_file:
        json.dump(result, ranking_file)

    return result


def sort_win_data():
    """
    A helper function that ranks all the teams no matter which conference they are in

    :return: A list containing tuples of (team abbreviation, number of wins)
    """
    # get data
    win_count_path = join(Main.SIMULATE_RESULT_PATH, 'win_count.json')
    with open(win_count_path) as win_count_file:
        win_data = dict(json.load(win_count_file))

    # sort the teams
    win_data_list = [(team_abb, num_win) for team_abb, num_win in win_data.items()]
    win_data_list.sort(key=lambda win: win[1], reverse=True)

    # return result
    return win_data_list


def rank_team_all():
    """
    This function calls sort_win_data() and creates a list containing only the
    team abbreviation but not the number of wins

    :return: A dictionary where the key is the team rank and the value is the team abbreviation
    """
    result = {}
    win_data_list = sort_win_data()
    for rank in range(30):
        result[rank + 1] = win_data_list[rank][0]

    return result
