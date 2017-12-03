import json

from django.shortcuts import render
from os.path import join
from data_retriever import Main


def boxscore_example(request):
    game_id = request.GET['gameID']

    path = join(Main.GAME_BASE_PATH, str(game_id) + '.json')
    with open(path) as boxscore_file:
        parsed_json = json.load(boxscore_file)
    resource = parsed_json['resource']
    parameters = parsed_json['parameters']
    result_sets = parsed_json['resultSets']

    player_headers = ['TEAM_ABBREVIATION', 'PLAYER_NAME', 'START_POSITION', 'MIN', 'PTS', 'OREB', 'DREB', 'REB', 'AST',
                      'STL', 'BLK', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'TO',
                      'PF', 'PLUS_MINUS']
    team_headers = ['TEAM_ABBREVIATION', 'GAME_ID', 'TEAM_ID', 'MIN', 'PTS', 'OREB', 'DREB', 'REB', 'AST',
                    'STL', 'BLK', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'TO', 'PF',
                    'PLUS_MINUS']
    headers = ['Team', 'Player Names', 'Position', 'MIN', 'PTS', 'OREB', 'DREB', 'REB', 'AST', 'STL',
               'BLK', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', '+/-']

    player_stats_index = []
    team_stats_index = []
    rows = []
    new_row = []

    player_result = find_player_result(result_sets)
    for k, v in player_result.items():
        if k == 'headers':
            all_player_headers = v
            for header in player_headers:
                player_stats_index.append(all_player_headers.index(header))
        elif k == 'rowSet':
            for row in v:
                for index in player_stats_index:
                    new_row.append(row[index])
                for i in range(len(new_row)):
                    if new_row[i] is None:
                        new_row[i] = 'DNP'
                rows.append(new_row)
                new_row = []

    team_result = find_team_result(result_sets)
    for k, v in team_result.items():
        if k == 'headers':
            all_team_headers = v
            for header in team_headers:
                team_stats_index.append(all_team_headers.index(header))
        elif k == 'rowSet':
            for row in v:
                for index in team_stats_index:
                    new_row.append(row[index])
                new_row[1] = 'N/A'
                new_row[2] = 'TOTAL:'
                rows.append(new_row)
                new_row = []

    return render(request, 'boxscore_example.html', {'headers': headers, 'rows': rows})


def load_file(file_name):
    file = open(file_name)
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
