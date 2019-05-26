"""
This module runs the season simulation and also initialize playoff brackets
"""

# general imports
import os.path
import os
from json import dump, load

from simulator import game_simulation as sim
from simulator.rank_teams import ranking_teams
from constant import GAME_LIST
from constant import TEAM_DICT
from constant import SIM_RANKING_PATH
from constant import SIM_PLAYOFF_PATH
from constant import SIM_RESULT_PATH


def run_simulation():
    """Runs season simulation and create data sets storing the results.

    :return: A tuple containing four data sets, each storing different results
    """
    # create variables
    results = {team_abb: {} for team_abb in TEAM_DICT.values()}
    win_count = {team_abb: 0 for team_abb in TEAM_DICT.values()}
    loss_count = {team_abb: 0 for team_abb in TEAM_DICT.values()}

    for team_abb in TEAM_DICT.values():
        other_teams = list(TEAM_DICT.values())
        other_teams.remove(team_abb)
        for other_team in other_teams:
            results[team_abb][other_team] = []

    counter = 0  # debug use variable

    # loop through the game list and simulate all the games
    for day in GAME_LIST:
        for game in day:
            team1_id = str(game[0])
            team2_id = str(game[1])
            simulator = sim.GameSimulation(team1_id, team2_id)
            team1_abb = TEAM_DICT[team1_id]
            team2_abb = TEAM_DICT[team2_id]
            counter += 1

            # check which team won the game
            if simulator.winner == team1_id:
                results[team1_abb][team2_abb].append('W')
                results[team2_abb][team1_abb].append('L')
                win_count[team1_abb] += 1
                loss_count[team2_abb] += 1
            elif simulator.winner == team2_id:
                results[team2_abb][team1_abb].append('W')
                results[team1_abb][team2_abb].append('L')
                win_count[team2_abb] += 1
                loss_count[team1_abb] += 1

    return results, win_count, loss_count, counter


def initialize_playoff():
    """This function initialize the playoff bracket that will be displayed on
    the web page

    :return: A test case use only dictionary containing the data to be displayed
    """
    # rank teams to create the team ranking files
    ranking_teams()

    # create variables
    final_result = {'east': {'teams': [], 'results': [[], [], []]},
                    'west': {'teams': [], 'results': [[], [], []]},
                    'final': {'teams': [], 'results': []}}
    rank_list = [[1, 8, 4, 5], [3, 6, 2, 7]]
    matchup = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}

    # reads the ranking file
    with open(SIM_RANKING_PATH) as ranking_file:
        ranking_data = load(ranking_file)

    # initialize the result data
    for division in ['east', 'west']:
        for teams in rank_list:
            check_list = teams.copy()
            for rank in teams:
                if rank in check_list:
                    team1 = ranking_data[division][str(rank)]
                    team2 = ranking_data[division][str(matchup[rank])]
                    final_result[division]['teams'].append([team1, team2])
                    check_list.remove(matchup[rank])

    # check if the file exist, if it does, then delete it and create a new one
    if os.path.exists(SIM_PLAYOFF_PATH):
        os.remove(SIM_PLAYOFF_PATH)

    with open(SIM_PLAYOFF_PATH, 'w') as playoff_file:
        dump(final_result, playoff_file)

    return final_result  # test case use only


def init():
    """Controls the simulations and initialize playoff data.

    :return: the result of the simulated regular season games
    """
    results = run_simulation()

    for team in TEAM_DICT.values():
        team_result = results[0][team]
        team_path = os.path.join(SIM_RESULT_PATH, team + '.json')
        with open(team_path, 'w') as result_file:
            dump(team_result, result_file)

    # create win count file
    win_count_path = os.path.join(SIM_RESULT_PATH, 'win_count.json')
    with open(win_count_path, 'w') as win_count_file:
        dump(results[1], win_count_file)

    # create loss count file
    loss_count_path = os.path.join(SIM_RESULT_PATH, 'loss_count.json')
    with open(loss_count_path, 'w') as loss_count_file:
        dump(results[2], loss_count_file)

    initialize_playoff()

    return results[0]
