from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from tournament import data_manipulate
from tournament.data_manipulate import format_data, second_third_round_data, conf_final_teams


class Tournament(APIView):
    def get(self, request, format=None):
        data = {'key', 'value'}
        return Response(data)


# @api_view(['GET', 'POST'])
@csrf_exempt
def tournament(request, season):
    """if season == "simulated":
        for div in ['east', 'west']:
            for idx in range(2):
                format_data(div, idx)

        final_teams = []
        for div in ['east', 'west']:
            final_team = second_third_round_data(conf_final_teams[div], div, 3)
            final_teams.append(final_team)

        second_third_round_data(final_teams, 'final', 1)
        data = data_manipulate.final_data

    else:"""
    for div in ['east', 'west']:
        for idx in range(2):
            format_data(div, idx)

    final_teams = []
    for div in ['east', 'west']:
        final_team = second_third_round_data(conf_final_teams[div], div, 3)
        final_teams.append(final_team)

    second_third_round_data(final_teams, 'final', 1)
    data = data_manipulate.final_data

    return JsonResponse(data)


def bracket(request, season):
    return render(request, 'bracket.html', {'season': season})
