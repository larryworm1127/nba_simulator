from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from json import load

from stats_brackets.bracket_data import BracketData
from stats_files import Main
from simulator.playoff_simulation import run_whole_simulation
from simulator.season_simulation import init


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
        bracket_data = BracketData()

        bracket_data.create_playoff_data()
        data = bracket_data.get_final_data()

    return JsonResponse(data)


def bracket(request, season):
    with open(Main.DIVISION_LIST_PATH) as division_file:
        division_dict = load(division_file)

    east_teams = {team: 'images/' + team + '.png' for team in division_dict['east']}
    west_teams = {team: 'images/' + team + '.png' for team in division_dict['west']}

    context = {'season': season,
               'east_teams': east_teams,
               'west_teams': west_teams,
               }

    return render(request, 'stats_brackets/bracket.html', context)


def simulate_playoff(request):
    return JsonResponse(run_whole_simulation())


def simulate_season(request):
    return JsonResponse(init())
