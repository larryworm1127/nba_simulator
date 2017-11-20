import json
import os
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from nba_simulator.settings import BASE_DIR


def all_team_statistics(request):
    d = load_file(os.path.join(BASE_DIR, 'assets/team_stats/season_stats/Combined.json'))
    parsed_json = json.loads(d)
    resource = parsed_json['resource']
    parameters = parsed_json['parameters']

    resultSets = parsed_json['resultSets']
    headers=['Rank','Team City','Team Name','W','L','PPG','FG%','3P%','DREB','OREB','AST','TOV','STL','BLK','PF']
    rows = []
    indexes = []
    new_row = []
    rank = 1
    for result in resultSets:        
        for k,v in result.items():
            if k == 'headers':
                indexes.append(v.index('TEAM_CITY'))
                indexes.append(v.index('TEAM_NAME'))
                indexes.append(v.index('WINS'))
                indexes.append(v.index('LOSSES'))
                indexes.append(v.index('PTS'))
                indexes.append(v.index('FG_PCT'))
                indexes.append(v.index('FG3_PCT'))
                indexes.append(v.index('DREB'))
                indexes.append(v.index('OREB'))
                indexes.append(v.index('AST'))
                indexes.append(v.index('TOV'))
                indexes.append(v.index('STL'))
                indexes.append(v.index('BLK'))
                indexes.append(v.index('PF'))
            elif k == 'rowSet':
                for row in v:
                    new_row.append(rank)
                    rank += 1
                    for i in range(len(indexes)):
                        new_row.append(row[indexes[i]])
                    rows.append(new_row)
                    new_row = []

    print(BASE_DIR)
    t = get_template('all_team_statistics.html')
    html = t.render(
        {'resource': resource, 'parameters': parameters, 'resultSets': result_sets, 'headers': headers, 'rows': rows})
    return HttpResponse(html)


def load_file(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data
