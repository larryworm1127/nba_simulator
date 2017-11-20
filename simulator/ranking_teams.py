# general imports
import json
from data_retriever import Main
from os.path import join

win_count_path = join(Main.SIMULATE_RESULT_PATH, 'win_count.json')
with open(win_count_path) as win_count_file:
    win_data = dict(json.load(win_count_file))

with open(Main.TEAM_DICT_PATH) as team_dict_file:
    team_dict = json.load(team_dict_file)

with open(Main.DIVISION_LIST_PATH) as division_list_file:
    division_list = json.load(division_list_file)

result = {'east': {}, 'west': {}}
team_list = team_dict.values()


def ranking_teams():
    win_data_list = [(team_abb, num_win) for team_abb, num_win in win_data.items()]
    print(win_data_list)

    win_data_list.sort(key=lambda win: win[1], reverse=True)
    print(win_data_list)
    east_counter = 1
    west_counter = 1
    for index in range(len(win_data_list)):
        team_abb = win_data_list[index][0]
        if team_abb in division_list['east']:
            result['east'][east_counter] = team_abb
            east_counter += 1
        else:
            result['west'][west_counter] = team_abb
            west_counter += 1

ranking_teams()
print(result)
