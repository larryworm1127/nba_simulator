from json import load
from os.path import join
from data_retriever import Main
from os import listdir

team_list = listdir(Main.TEAM_SEASON_PATH)


def top_ten_wlr():
    wlr_list = get_data()[0]
    wlr_list.sort(key=lambda ratio: ratio[1], reverse=True)
    return wlr_list


def top_ten_points():
    points_list = get_data()[1]
    points_list.sort(key=lambda ratio: ratio[1], reverse=True)
    return points_list


def top_ten_rebounds():
    rebounds_list = get_data()[2]
    rebounds_list.sort(key=lambda ratio: ratio[1], reverse=True)
    return rebounds_list


def top_ten_assists():
    assists_list = get_data()[3]
    assists_list.sort(key=lambda ratio: ratio[1], reverse=True)
    return assists_list


def get_data():
    wlr_list = []
    points_list = []
    rebounds_list = []
    assists_list = []

    for team_dir in team_list:
        with open(join(Main.TEAM_SEASON_PATH, team_dir)) as team_season_file:
            data = load(team_season_file)

        win_loss_ratios = data['resultSets'][0]['rowSet'][-2][7]
        wlr_list.append((team_dir[:3], win_loss_ratios))

        points_per_game = data['resultSets'][0]['rowSet'][-2][-2]
        points_list.append((team_dir[:3], points_per_game))

        rebounds_per_game = round(data['resultSets'][0]['rowSet'][-2][-9] + data['resultSets'][0]['rowSet'][-2][-10], 2)
        rebounds_list.append((team_dir[:3], rebounds_per_game))

        assists_per_game = data['resultSets'][0]['rowSet'][-2][-7]
        assists_list.append((team_dir[:3], assists_per_game))

    return wlr_list, points_list, rebounds_list, assists_list

