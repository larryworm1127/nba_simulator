import json

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from data_retriever import Main
import os

tempList = []


def all_team_statistics(request):
    headers = ['Team City', 'Team Name', 'W', 'L', 'PPG', 'FG%', '3P%', 'DREB', 'OREB', 'AST', 'TOV', 'STL', 'BLK',
               'PF']
    rows = []
    indexes = []
    new_row = []

    d = loadFile(os.path.join(Main.TEAM_SEASON_PATH, 'ATL.json'))
    parsed_json = json.loads(d)
    resultSets = parsed_json['resultSets']

    tempList = getData()
    sortData(tempList)

    for row in tempList:
        indexes = findIndexes(resultSets)
        for i in range(len(indexes)):
            new_row.append(row[indexes[i]])
        rows.append(new_row)
        new_row = []
        indexes = []

    t = get_template('all_team_statistics.html')
    html = t.render({'resultSets': resultSets, 'headers': headers, 'rows': rows})
    return HttpResponse(html)


def findIndexes(resultSets):
    headers = ['TEAM_CITY', 'TEAM_NAME', 'WINS', 'LOSSES', 'PTS', 'FG_PCT', 'FG3_PCT', 'DREB', 'OREB', 'AST', 'TOV',
               'STL', 'BLK', 'PF']
    indexes = []
    for result in resultSets:
        for k, v in result.items():
            if k == 'headers':
                for h in range(len(headers)):
                    indexes.append(v.index(headers[h]))
    return (indexes)


def getData():
    allTeamLists = []
    for eachFile in os.listdir(Main.TEAM_SEASON_PATH):
        d = loadFile(os.path.join(Main.TEAM_SEASON_PATH, eachFile))
        parsed_json = json.loads(d)
        resultSets = parsed_json['resultSets']
        for result in resultSets:
            for k, v in result.items():
                if k == 'rowSet':
                    for row in v:
                        if row[3] == "2016-17":
                            allTeamLists.append(row)
    return allTeamLists


def sortData(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if (l[j])[5] < (l[j + 1])[5]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp


def loadFile(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data
