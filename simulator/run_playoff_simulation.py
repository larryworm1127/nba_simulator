# general imports
from data_retriever import Main
from simulator import one_game_simulation
from os.path import join
from json import dump, load

# constants
TEAM_MATCH_LIST = [[1, 8, 4, 5], [3, 6, 2, 7]]
TEAM_OPPONENT = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}

with open(Main.SIMULATE_RANKING_PATH) as ranking_file:
    ranking_data = dict(load(ranking_file))

with open(Main.TEAM_DICT_PATH) as team_dict_file:
    team_dict = load(team_dict_file)


def run_single_series(team1, team2):
    """
    Takes two team IDs and run the 7 games playoff series

    :param team1: the team ID of team one
    :param team2: the team ID of team two
    :return: A list containing two tuples, each tuple contains the team ID and its score
    """
    series_complete = False
    team1_points, team2_points = (0, 0)
    result = []

    while not series_complete:
        simulate = one_game_simulation.TeamScoringMachine(team1, team2)
        winner = simulate.get_winner()

        if winner == team1:
            team1_points += 1
        else:
            team2_points += 1

        if team1_points == 4 or team2_points == 4:
            series_complete = True

    result.append((team1, team1_points))
    result.append((team2, team2_points))
    return result


def run_round_simulation(teams, round_num, index=None):
    """
    Takes a list of teams and run a round of
    series depending on the round number

    :param teams: a list of teams in format of {1: 'GSW', 2: 'SAS', etc}
    :param round_num: the round number
    :param index: index used for first round simulation
    :return: the result of the simulation and the teams that made into next round
    """
    result = []
    next_round_teams = []
    if round_num == 3 or round_num == 4:
        team1_abb = list(teams.values())[0] if round_num == 3 else teams[0]
        team2_abb = list(teams.values())[1] if round_num == 3 else teams[1]
        team1_id = Main.get_id_from_abb(team1_abb)
        team2_id = Main.get_id_from_abb(team2_abb)
        series_result = run_single_series(team1_id, team2_id)
        result.append(series_result)
        next_round_teams.append(team_dict[team1_id]) if series_result[1][1] > series_result[0][
            1] else next_round_teams.append(team_dict[team2_id])

    else:
        loop = []
        if round_num == 1:
            team_check_list = TEAM_MATCH_LIST[index].copy()
            loop = TEAM_MATCH_LIST[index]
        elif round_num == 2:
            team_check_list = list(teams.keys())
            loop = list(teams.keys())

        for team_rank in loop:
            if team_rank in team_check_list:
                team_abb = teams[team_rank]
                opponent_rank = TEAM_OPPONENT[team_rank] if round_num == 1 else loop[loop.index(team_rank) + 1]
                opponent = teams[opponent_rank]
                team_id = Main.get_id_from_abb(team_abb)
                opponent_id = Main.get_id_from_abb(opponent)
                series_result = run_single_series(team_id, opponent_id)
                team_check_list.remove(opponent_rank)
                next_round_teams.append(team_rank) if series_result[0][1] > series_result[1][
                    1] else next_round_teams.append(TEAM_OPPONENT[team_rank])
                result.append(series_result)

    return result, next_round_teams


def run_whole_simulation():
    playoff_teams = get_playoff_teams()
    result = {'east': {'teams': [], 'results': [[], [], []]}, 'west': {'teams': [], 'results': [[], [], []]},
              'final': {'teams': [], 'results': []}}
    final_teams = []

    for division in ['east', 'west']:
        next_round_teams = []

        # first round simulation
        for index in range(2):
            teams = playoff_teams[division]
            round_one_result = run_round_simulation(teams, 1, index)
            team_scores = round_one_result[0]
            next_round_teams.extend(round_one_result[1])
            for idx in range(2):
                result[division]['teams'].append([team_dict[team_scores[idx][0][0]], team_dict[team_scores[idx][1][0]]])
                result[division]['results'][0].append([team_scores[idx][0][1], team_scores[idx][1][1]])

        # second round simulation
        teams = {}
        for rank in next_round_teams:
            teams[rank] = playoff_teams[division][rank]
        round_two_result = run_round_simulation(teams, 2)
        team_scores = round_two_result[0]
        next_round_teams = round_two_result[1]
        result[division]['results'][1].append([team_scores[0][0][1], team_scores[0][1][1]])
        result[division]['results'][1].append([team_scores[1][0][1], team_scores[1][1][1]])

        # conference final simulation
        teams = {}
        for rank in next_round_teams:
            teams[rank] = playoff_teams[division][rank]
        third_round_result = run_round_simulation(teams, 3)
        team_scores = third_round_result[0]
        final_teams.append(third_round_result[1][0])
        result[division]['results'][2].append([team_scores[0][0][1], team_scores[0][1][1]])

    # final simulation
    final_round_result = run_round_simulation(final_teams, 4)
    team_scores = final_round_result[0]
    result['final']['teams'].append(final_teams)
    result['final']['results'].append([team_scores[0][0][1], team_scores[0][1][1]])

    # put the simulated results into file
    with open(Main.SIMULATE_PLAYOFF_PATH, 'w') as playoff_file:
        dump(result, playoff_file)

    return result  # test cases use only


def get_playoff_teams():
    result = {'east': {}, 'west': {}}
    for div in ['east', 'west']:
        for rank in range(1, 9):
            result[div][rank] = ranking_data[div][str(rank)]

    return result
