from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from tournament import data_manipulate
from data_retriever import Main
from json import load
from simulator import run_playoff_simulation


class Tournament(APIView):
    def get(self, request, format=None):
        data = {'key', 'value'}
        return Response(data)


# @api_view(['GET', 'POST'])
@csrf_exempt
def tournament(request, season):
    if season == "2018":
        #run_playoff_simulation.run_whole_simulation()
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
    return render(request, 'bracket.html', {'season': season})
