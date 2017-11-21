import json
import os
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from data_retriever import Main


def all_team_statistics(request):
    with open(Main.COMBINE_FILE_PATH) as combine_file:
        parsed_json = json.load(combine_file)
    resource = parsed_json['resource']
    parameters = parsed_json['parameters']

    result_sets = parsed_json['resultSets']
    headers=['Rank','Team City','Team Name','W','L','PPG','FG%','3P%','DREB','OREB','AST','TOV','STL','BLK','PF']
    rows = []
    indexes = []
    new_row = []
    rank = 1
    for result in result_sets:        
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

    t = get_template('all_team_statistics.html')
    html = t.render(
        {'resource': resource, 'parameters': parameters, 'resultSets': result_sets, 'headers': headers, 'rows': rows})
    return HttpResponse(html)


def load_file(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data
