# general import
from json import load
from data_retriever import Main, file_check
from os import listdir
from os.path import join

# constant
TEAM_MATCH_LIST = [[1, 8, 4, 5], [3, 6, 2, 7]]
TEAM_OPPONENT = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}

# create other variables and access data from files
final_data = {'east': {'teams': [], 'results': [[], [], []]}, 'west': {'teams': [], 'results': [[], [], []]},
              'final': {'teams': [], 'results': [[]]}}

file_check.init()

with open(Main.DIVISION_LIST_PATH, 'r') as division_file:
    division_dict = load(division_file)

playoff_teams_list = [file.split('.')[0] for file in listdir(Main.TEAM_PLAYOFF_PATH)]
playoff_dict = {'east': {}, 'west': {}}
div_list = {}
for team_name in playoff_teams_list:
    with open(join(Main.TEAM_SEASON_PATH, team_name + '.json'), 'r') as season_file:
        data = load(season_file)
        team_division = 'east' if team_name in division_dict['east'] else 'west'
        div_list[team_name] = team_division

    playoff_dict[team_division][data['resultSets'][0]['rowSet'][-2][8]] = team_name

conf_final_teams = {'east': [], 'west': []}


# format first round data
def format_data(division, index):
    team_check_list = TEAM_MATCH_LIST[index].copy()
    next_round_teams = []
    for team in TEAM_MATCH_LIST[index]:
        team_abb = playoff_dict[division][team]

        with open(join(Main.TEAM_PLAYOFF_PATH, team_abb + '.json')) as playoff_file:
            team_data = load(playoff_file)

        opponent = playoff_dict[division][TEAM_OPPONENT[team]]
        team_check_list.remove(TEAM_OPPONENT[team])
        if team in team_check_list:
            final_data[division]['teams'].append([team_abb, opponent])

            team_points = 0
            opponent_points = 0
            for index in range(len(team_data['resultSets'][0]['rowSet']) - 1, -1, -1):
                if team_data['resultSets'][0]['rowSet'][index][3][-3:] == opponent:
                    if team_data['resultSets'][0]['rowSet'][index][4] == 'W':
                        team_points += 1
                    else:
                        opponent_points += 1

            final_data[division]['results'][0].append([team_points, opponent_points])

            if team_points > opponent_points:
                next_round_teams.append(team_abb)
            else:
                next_round_teams.append(opponent)

    next_round_team = second_third_round_data(next_round_teams, division, 2)
    conf_final_teams[division].append(next_round_team)


# format second and third round data
def second_third_round_data(team_list, division, round_num):
    team_abb = team_list[0]
    opponent = team_list[1]

    with open(join(Main.TEAM_PLAYOFF_PATH, team_abb + '.json')) as playoff_file:
        team_data = load(playoff_file)

    if division == 'final':
        final_data[division]['teams'].append([team_abb, opponent])

    team_points = 0
    opponent_points = 0
    for index in range(len(team_data['resultSets'][0]['rowSet']) - 1, -1, -1):
        if team_data['resultSets'][0]['rowSet'][index][3][-3:] == opponent:
            if team_data['resultSets'][0]['rowSet'][index][4] == 'W':
                team_points += 1
            else:
                opponent_points += 1

    final_data[division]['results'][round_num - 1].append([team_points, opponent_points])
    return team_abb if team_points > opponent_points else opponent


def create_playoff_data():
    for div in ['east', 'west']:
        for idx in range(2):
            format_data(div, idx)

    final_teams = []
    for div in ['east', 'west']:
        final_team = second_third_round_data(conf_final_teams[div], div, 3)
        final_teams.append(final_team)

    second_third_round_data(final_teams, 'final', 1)
