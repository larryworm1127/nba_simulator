import json
import os
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from nba_simulator.settings import BASE_DIR

def boxscore_example(request):
    gameID = request.GET['gameID']
    file_name = "assets/game_stats/%s.json" %gameID
    d = load_file( os.path.join(BASE_DIR, file_name))
    parsed_json = json.loads(d)
    resource = parsed_json['resource']
    parameters = parsed_json['parameters']
    result_sets = parsed_json['resultSets']

    player_headers = ['TEAM_ABBREVIATION','PLAYER_NAME','START_POSITION','MIN','PTS','OREB','DREB','REB','AST',
               'STL','BLK','FGM','FGA','FG_PCT','FG3M','FG3A','FG3_PCT','FTM','FTA','FT_PCT','TO','PF','PLUS_MINUS']
    team_headers = ['TEAM_ABBREVIATION','GAME_ID','TEAM_ID','MIN','PTS','OREB','DREB','REB','AST',
               'STL','BLK','FGM','FGA','FG_PCT','FG3M','FG3A','FG3_PCT','FTM','FTA','FT_PCT','TO','PF','PLUS_MINUS']
    headers = ['TEAM_INITIALS','INDIVIDUAL_PLAYER_NAMES','P','MIN','PTS','OREB','DREB','REB','AST','STL','BLK','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','TOV','PF','+/-']

    player_stats_index = []
    team_stats_index = []
    rows = []
    new_row = []

    player_result = find_player_result(result_sets)
    for k, v in player_result.items():
        if k == 'headers':
            all_player_headers = v
            for i in range(len(player_headers)):
                player_stats_index.append(all_player_headers.index(player_headers[i]))
        elif k == 'rowSet':
            for row in v:
                for i in range(len(player_stats_index)):
                    new_row.append(row[player_stats_index[i]])
                for i in range(len(new_row)):
                    if new_row[i] == None:
                        new_row[i] = 'DNP'
                rows.append(new_row)
                new_row = []

    team_result = find_team_result(result_sets)
    for k, v in team_result.items():
        if k == 'headers':
            all_team_headers = v
            for i in range(len(team_headers)):
                team_stats_index.append(all_team_headers.index(team_headers[i]))
        elif k == 'rowSet':
            for row in v:
                for i in range(len(team_stats_index)):
                    new_row.append(row[team_stats_index[i]])
                new_row[1] = 'N/A'
                new_row[2] = 'TOTAL:'
                rows.append(new_row)
                new_row = []
 
    print(BASE_DIR)
    t = get_template('boxscore_example.html')
    html = t.render({'resource': resource, 'parameters': parameters, 'resultSets': result_sets, 'headers':headers, 'rows':rows}) 
    return HttpResponse(html)

def load_file(file_name):
       file =  open(file_name)
       data = file.read()
       file.close()
       return data

def find_player_result(result_sets):
    for result in result_sets:
        for k, v in result.items():           
            if v == 'PlayerStats':
                return result

def find_team_result(result_sets):
    for result in result_sets:
        for k, v in result.items():           
            if v == 'TeamStats':
                return result
