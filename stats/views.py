from django.shortcuts import render
from stats.game_stats_data import create_data
from stats.all_team_data import create_team_data
from stats.wins_losses import create_wl_data


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

    return render(request, 'stats/boxscore.html', {'headers': headers,
                                                   'rows1': rows1,
                                                   'rows2': rows2,
                                                   'team1_name': team1_name,
                                                   'team2_name': team2_name,
                                                   'team1': team1,
                                                   'team2': team2})


def all_team_stats(request):
    data = create_team_data()
    headers = data[0]
    rows = data[1]

    return render(request, 'stats/all_team_statistics.html', {'headers': headers, 'rows': rows})


def wins_and_losses(request):
    data = create_wl_data()
    headers = data[0]
    rows = data[1]

    return render(request, 'stats/wins_losses.html', {'headers': headers, 'rows': rows})


def simulated_standing(request):

    pass