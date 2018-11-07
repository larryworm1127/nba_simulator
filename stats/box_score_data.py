"""This module creates box score page data"""

# general imports
from os.path import join
from stats_files import GAME_BASE_PATH
from json import load


# main functions
def create_data(game_id):
    path = join(GAME_BASE_PATH, str(game_id) + '.json')
    with open(path) as boxscore_file:
        parsed_json = load(boxscore_file)

    result_sets = parsed_json['resultSets']

    player_headers = ['TEAM_ABBREVIATION', 'PLAYER_NAME', 'START_POSITION',
                      'MIN', 'PTS', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK',
                      'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM',
                      'FTA', 'FT_PCT', 'TO', 'PF', 'PLUS_MINUS']
    team_headers = ['TEAM_ABBREVIATION', 'TEAM_CITY', 'TEAM_NAME', 'MIN', 'PTS',
                    'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'FGM', 'FGA',
                    'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                    'TO', 'PF', 'PLUS_MINUS']
    headers = ['Team', 'Player Names', 'P', 'MIN', 'PTS', 'OREB', 'DREB', 'REB',
               'AST', 'STL', 'BLK', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%',
               'FTM', 'FTA', 'FT%', 'TOV', 'PF', '+/-']

    player_stats_index = []
    team_stats_index = []
    rows1 = []
    rows2 = []
    new_row = []
    counter1 = 0
    counter2 = []
    counter3 = 0
    counter4 = 0

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
                rows1.append(new_row)
                rows2.append(new_row)
                new_row = []

    for _ in rows1:
        if (rows1[0])[0] != (rows1[counter1])[0]:
            counter2.append(counter1)
        counter1 += 1
    for row in counter2:
        rows1.remove(rows1[row - counter3])
        counter3 += 1
    while counter4 < counter2[0]:
        rows2.remove(rows2[0])
        counter4 += 1

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
                rows1.append(new_row)
                new_row = []

    if (rows1[len(rows1) - 2][0]) != rows1[0][0]:
        rows2.append(rows1[len(rows1) - 2])
        rows1.remove(rows1[len(rows1) - 2])
    else:
        rows2.append(rows1[len(rows1) - 1])
        rows1.remove(rows1[len(rows1) - 1])

    team1_name = (rows1[len(rows1) - 1])[1] + ' ' + (rows1[len(rows1) - 1])[2]
    team2_name = (rows2[len(rows2) - 1])[1] + ' ' + (rows2[len(rows2) - 1])[2]
    team1 = rows1[0][0]
    team2 = rows2[0][0]

    for row in rows1:
        row.remove(row[0])
    for row in rows2:
        row.remove(row[0])
    headers.remove(headers[0])

    rows1[len(rows1) - 1][0] = 'TOTAL:'
    rows1[len(rows1) - 1][1] = ''
    rows2[len(rows2) - 1][0] = 'TOTAL:'
    rows2[len(rows2) - 1][1] = ''

    return headers, rows1, rows2, team1_name, team2_name, team1, team2


def find_player_result(result_sets):
    for result in result_sets:
        for _, v in result.items():
            if v == 'PlayerStats':
                return result


def find_team_result(result_sets):
    for result in result_sets:
        for _, v in result.items():
            if v == 'TeamStats':
                return result
