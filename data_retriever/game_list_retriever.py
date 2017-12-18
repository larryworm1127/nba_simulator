# general imports
from nba_py import Scoreboard
from json import dump
from os.path import exists
from datetime import timedelta, date
from data_retriever import Main


def date_range(start, end):
    for n in range(int((end - start).days)):
        yield start + timedelta(n)


def create_game_list_files():
    print("Create game list files ...")
    start_date = date(2017, 10, 17)
    end_date = date(2018, 4, 12)

    date_list = []
    for single_date in date_range(start_date, end_date):
        date_list.append(str(single_date).split('-'))

    game_list = []

    for day in date_list:
        games = []
        score_board = Scoreboard(month=int(day[1]), day=int(day[2]), year=int(day[0])).game_header()

        for item in score_board:
            print(str(day) + ": " + str(item['HOME_TEAM_ID']) + ', ' + str(item['VISITOR_TEAM_ID']))
            if item['HOME_TEAM_ID']:
                games.append((item['HOME_TEAM_ID'], item['VISITOR_TEAM_ID']))

        if games:
            game_list.append(games)

    with open(Main.GAME_LIST_PATH, 'w') as outfile:
        dump(game_list, outfile)


def init():
    if not exists(Main.GAME_LIST_PATH):
        create_game_list_files()
