from json import load
from os.path import join
from data_retriever import Main
from os import listdir

team_list = listdir(Main.TEAM_SEASON_PATH)


def top_ten():
    for team_dir in team_list:
        with open(join(Main.TEAM_SEASON_PATH, team_dir)) as team_season_file:
            data = load(team_season_file)

        win_loss_ratios = data['resultSets'][0]['rowSet'][-2][7]
        points_per_game = data['resultSets'][0]['rowSet'][-2][-2]
        rebounds_per_game = round(data['resultSets'][0]['rowSet'][-2][-9] + data['resultSets'][0]['rowSet'][-2][-10], 2)
        assists_per_game = data['resultSets'][0]['rowSet'][-2][-7]

        wlr_list = [(team_abb, wlr) for team_abb, wlr in data.items()]
        copy_wlr = win_loss_ratios
        top_ten_wlr = {}

        wlr_list.sort(key=lambda win: win[1])
        for item in wlr_list:
            team_abb = item[0]
            print(team_abb)

        """
        while len(top_ten_wlr) <= 10:
            largest = max(win_loss_ratios[0])
            top_ten_wlr.update(largest)
            copy_wlr.remove(largest)
        len(top_ten_wlr > 10)

        print(copy_wlr)"""


top_ten()





