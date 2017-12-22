from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from tournament import data_manipulate
from tournament.data_manipulate import division_dict
from data_retriever import Main
from json import load
from simulator.run_playoff_simulation import run_whole_simulation
from simulator.run_season_simulation import init, initialize_playoff


class Tournament(APIView):
    def get(self, request, format=None):
        data = {'key', 'value'}
        return Response(data)


# @api_view(['GET', 'POST'])
@csrf_exempt
def tournament(request, season):
    data = None
    if season == "2017-18":
        with open(Main.SIMULATE_PLAYOFF_PATH, 'r+') as playoff_file:
            data = load(playoff_file)

    elif season == "2016-17":
        data_manipulate.final_data = {'east': {'teams': [], 'results': [[], [], []]},
                                      'west': {'teams': [], 'results': [[], [], []]},
                                      'final': {'teams': [], 'results': [[]]}}
        data_manipulate.create_playoff_data()
        data = data_manipulate.final_data

    return JsonResponse(data)


def bracket(request, season):
    east_teams = {team: 'images/' + team + '.png' for team in division_dict['east']}
    west_teams = {team: 'images/' + team + '.png' for team in division_dict['west']}

    context = {'season': season,
               'east_teams': east_teams,
               'west_teams': west_teams,
               }

    return render(request, 'tournament/bracket.html', context)


def simulate_playoff(request):
    return JsonResponse(run_whole_simulation())


def simulate_season(request):
    return JsonResponse(init())
