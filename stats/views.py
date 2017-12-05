from django.shortcuts import render
from stats.game_stats_data import create_data
from stats.all_team_data import create_team_data


def boxscore(request):
    game_id = request.GET['gameID']
    data = create_data(game_id)
    headers = data[0]
    rows = data[1]

    return render(request, 'stats/boxscore.html', {'headers': headers, 'rows': rows})


def all_team_stats(request):
    data = create_team_data()
    headers = data[0]
    rows = data[1]

    return render(request, 'stats/all_team_statistics.html', {'headers': headers, 'rows': rows})