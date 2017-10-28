from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView


class Tournament(APIView):
    def get(self, request, format=None):
        data = {'key', 'value'}
        return Response(data)


# @api_view(['GET', 'POST'])
@csrf_exempt
def tournament(request, season):
    if season == '2017':
        data = {
            "teams": [
                ["Team 1", "Team 2"],
                ["Team 3", "Team 4"]
            ],
            "results": [[
                [[1, 2], [3, 4]],
                [[5, 6]]
            ],
                [
                    [[7, 8]],
                    [[9, 10]]
                ],
                [
                    [
                        [11, 12],
                        [13, 14]
                    ],
                    [
                        [15, 16]
                    ]
                ]
            ]
        }
    else:
        data = {
            "teams": [
                ["Team 1", "Team 2"],
                ["Team 3", "Team 4"]
            ],
            "results": [
                [
                    [
                        [1, 2],
                        [3, 4]
                    ],
                    [
                        [5, 6],
                        [7, 8]
                    ]
                ]
            ]
        }
    return JsonResponse(data)


def bracket(request, season):
    return render(request, 'bracket.html', {'season': season})
