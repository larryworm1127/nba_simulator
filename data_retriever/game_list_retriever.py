# general imports
import nba_py
import json
from datetime import timedelta, date
from data_retriever import Main


def date_range(start, end):
    for n in range(int((end - start).days)):
        yield start + timedelta(n)

start_date = date(2017, 10, 17)
end_date = date(2018, 4, 12)

date_list = []
for single_date in date_range(start_date, end_date):
    date_list.append(str(single_date).split('-'))

print("Create game list files ...")


def create_game_list_files():
    game_list = []

    for index in range(len(date_list)):
        games = []
        day = date_list[index]
        score_board = nba_py.Scoreboard(month=int(day[1]), day=int(day[2]), year=int(day[0])).game_header()

        for item in score_board:
            print(str(day) + ": " + str(item['HOME_TEAM_ID']) + ', ' + str(item['VISITOR_TEAM_ID']))
            if item['HOME_TEAM_ID']:
                games.append((item['HOME_TEAM_ID'], item['VISITOR_TEAM_ID']))

        if games:
            game_list.append(games)

    with open(Main.GAME_LIST_PATH, 'w') as outfile:
        json.dump(game_list, outfile)


def init():
    create_game_list_files()

init()
