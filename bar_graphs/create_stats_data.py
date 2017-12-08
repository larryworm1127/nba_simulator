# general imports
from json import load
from os.path import join
from data_retriever import Main
from os import listdir

team_list = listdir(Main.TEAM_SEASON_PATH)


for team_dir in team_list:
    with open(join(Main.TEAM_SEASON_PATH, team_dir)) as team_season_file:
        data = load(team_season_file)

    win_loss_ratios = data['resultSets'][0]['rowSet'][-2][7]
    points_per_game = data['resultSets'][0]['rowSet'][-2][-2]
    """rebounds_per_game = data['resultSets'][0]['rowSet'][-2][7]"""
    assists_per_game = data['resultSets'][0]['rowSet'][-2][-7]

    print(win_loss_ratios)
