"""
This module runs the season simulation and also initialize playoff brackets
"""

# general imports
from os.path import join, exists
from os import remove
from json import dump, load

from stats_files import Main, create_other_files
from simulator import game_simulation as sim
from simulator.rank_teams import ranking_teams

create_other_files.init()

with open(Main.GAME_LIST_PATH, 'r') as game_list_file:
    game_list = load(game_list_file)

with open(Main.TEAM_DICT_PATH, 'r') as team_dict_file:
    team_dict = dict(load(team_dict_file))


def run_simulation():
    """
    Runs season simulation and create data sets storing the results

    :return: A tuple containing four different data set, each storing different results
    """
    # create variables
    results = {team_abb: {} for team_abb in team_dict.values()}
    win_count = {team_abb: 0 for team_abb in team_dict.values()}
    loss_count = {team_abb: 0 for team_abb in team_dict.values()}

    for team_abb in team_dict.values():
        other_teams = list(team_dict.values())
        other_teams.remove(team_abb)
        for other_team in other_teams:
            results[team_abb][other_team] = []

    # print a message to let the user know the simulation is running
    print("Running simulation ...")

    counter = 0  # debug use variable

    # loop through the game list and simulate all the games
    for day in game_list:
        for game in day:
            team1_id = str(game[0])
            team2_id = str(game[1])
            simulator = sim.GameSimulation(team1_id, team2_id)
            team1_abb = team_dict[team1_id]
            team2_abb = team_dict[team2_id]
            counter += 1

            # check which team won the game
            if simulator.get_winner() == team1_id:
                results[team1_abb][team2_abb].append('W')
                results[team2_abb][team1_abb].append('L')
                win_count[team1_abb] += 1
                loss_count[team2_abb] += 1
            elif simulator.get_winner() == team2_id:
                results[team2_abb][team1_abb].append('W')
                results[team1_abb][team2_abb].append('L')
                win_count[team2_abb] += 1
                loss_count[team1_abb] += 1

    return results, win_count, loss_count, counter


def initialize_playoff():
    """
    This function initialize the playoff bracket that will be displayed on the web page

    :return: A test case use only dictionary containing the data to be displayed
    """
    # rank teams to create the team ranking files
    ranking_teams()

    # create variables
    final_result = {'east': {'teams': [], 'results': [[], [], []]}, 'west': {'teams': [], 'results': [[], [], []]},
                    'final': {'teams': [], 'results': []}}
    team_match_list = [[1, 8, 4, 5], [3, 6, 2, 7]]
    team_opponent = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}

    # reads the ranking file
    with open(Main.SIMULATE_RANKING_PATH) as ranking_file:
        ranking_data = load(ranking_file)

    # initialize the result data
    for division in ['east', 'west']:
        for teams in team_match_list:
            check_list = teams.copy()
            for rank in teams:
                if rank in check_list:
                    team1 = ranking_data[division][str(rank)]
                    team2 = ranking_data[division][str(team_opponent[rank])]
                    final_result[division]['teams'].append([team1, team2])
                    check_list.remove(team_opponent[rank])

    # check if the file exist, if it does, then delete it and create a new one
    if exists(Main.SIMULATE_PLAYOFF_PATH):
        remove(Main.SIMULATE_PLAYOFF_PATH)
    with open(Main.SIMULATE_PLAYOFF_PATH, 'w') as playoff_file:
        dump(final_result, playoff_file)

    return final_result  # test case use only


def init():
    """
    Controls the simulations and initialize playoff data

    :return: the result of the simulated regular season games
    """
    results = run_simulation()

    for team in team_dict.values():
        team_result = results[0][team]
        team_path = join(Main.SIMULATE_RESULT_PATH, team + '.json')
        with open(team_path, 'w') as result_file:
            dump(team_result, result_file)

    # create win count file
    win_count_path = join(Main.SIMULATE_RESULT_PATH, 'win_count.json')
    with open(win_count_path, 'w') as win_count_file:
        dump(results[1], win_count_file)

    # create loss count file
    loss_count_path = join(Main.SIMULATE_RESULT_PATH, 'loss_count.json')
    with open(loss_count_path, 'w') as loss_count_file:
        dump(results[2], loss_count_file)

    initialize_playoff()

    return results[0]
