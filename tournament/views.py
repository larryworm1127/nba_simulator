from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from tournament import data_manipulate
from tournament.data_manipulate import division_dict
from data_retriever import Main
from json import load


class Tournament(APIView):
    def get(self, request, format=None):
        data = {'key', 'value'}
        return Response(data)


# @api_view(['GET', 'POST'])
@csrf_exempt
def tournament(request, season):
    if season == "2018":
        with open(Main.SIMULATE_PLAYOFF_PATH) as playoff_file:
            data = load(playoff_file)

    else:
        data_manipulate.final_data = {'east': {'teams': [], 'results': [[], [], []]},
                                      'west': {'teams': [], 'results': [[], [], []]},
                                      'final': {'teams': [], 'results': [[]]}}
        data_manipulate.create_playoff_data()
        data = data_manipulate.final_data

    return JsonResponse(data)


def bracket(request, season):
    east_teams = {team: 'images/' + team + '.png' for team in division_dict['east']}
    west_teams = {team: 'images/' + team + '.png' for team in division_dict['west']}

    return render(request, 'tournament/bracket.html',
                  {'season': season,
                   'east_teams': east_teams,
                   'west_teams': west_teams,
                   })
