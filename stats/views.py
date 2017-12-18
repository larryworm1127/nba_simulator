from django.shortcuts import render

from stats.game_stats_data import create_data
from stats.all_team_data import create_team_data
from stats.standing_data import create_standing_data


def main_page(request):
    return render(request, 'stats/main_page.html')


def boxscore(request):
    game_id = request.GET['gameID']
    data = create_data(game_id)
    headers = data[0]
    rows1 = data[1]
    rows2 = data[2]
    team1_name = data[3]
    team2_name = data[4]
    team1 = data[5]
    team2 = data[6]

    return render(request, 'stats/boxscore.html',
                  {'headers': headers,
                   'rows1': rows1,
                   'rows2': rows2,
                   'team1_name': team1_name,
                   'team2_name': team2_name,
                   'team1': team1,
                   'team2': team2})


def all_team_stats(request):
    sort = request.GET.get('sort')
    data = create_team_data(sort)
    headers = data['headers']
    rows = data['rows']

    return render(request, 'stats/all_team_statistics.html',
                  {'headers': headers,
                   'rows': rows,
                   })


def standing(request, season):
    data = create_standing_data(season)
    headers = data[0]
    rows = data[1]

    if season == '2017-18':
        template = 'stats/simulated_standing.html'
    else:
        template = 'stats/standing.html'

    return render(request, template,
                  {'headers': headers,
                   'rows': rows,
                   'season': season
                   })

