# general imports
from data_retriever import Main
from simulator import one_game_simulation
from os.path import join
import json

with open(Main.GAME_LIST_PATH, 'r') as game_list_file:
    game_list = json.load(game_list_file)

with open(Main.TEAM_DICT_PATH, 'r') as team_dict_file:
    team_dict = dict(json.load(team_dict_file))


def run_simulation():
    results = {team_abb: {} for team_abb in team_dict.values()}
    win_count = {team_abb: 0 for team_abb in team_dict.values()}
    loss_count = {team_abb: 0 for team_abb in team_dict.values()}

    for team_abb in team_dict.values():
        other_teams = list(team_dict.values())
        other_teams.remove(team_abb)
        for other_team in other_teams:
            results[team_abb][other_team] = []

    print("Running simulation ...")

    counter = 0
    for day in range(len(game_list)):
        for game in range(len(game_list[day])):
            team1_id = str(game_list[day][game][0])
            team2_id = str(game_list[day][game][1])
            simulator = one_game_simulation.TeamScoringMachine(team1_id, team2_id)
            team1_abb = team_dict[team1_id]
            team2_abb = team_dict[team2_id]
            counter += 1

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


def init():
    results = run_simulation()

    for team in team_dict.values():
        team_result = results[0][team]
        team_path = join(Main.SIMULATE_RESULT_PATH, team + '.json')
        with open(team_path, 'w') as result_file:
            json.dump(team_result, result_file)

    win_count_path = join(Main.SIMULATE_RESULT_PATH, 'win_count.json')
    with open(win_count_path, 'w') as win_count_file:
        json.dump(results[1], win_count_file)

    loss_count_path = join(Main.SIMULATE_RESULT_PATH, 'loss_count.json')
    with open(loss_count_path, 'w') as loss_count_file:
        json.dump(results[2], loss_count_file)

#init()
