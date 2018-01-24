from django.shortcuts import render

from stats_team_pages.team_page_data import *


def season_games(request, team, season):
    team_logo = "images/" + team + ".png"
    team_name = get_team_from_abb(team)
    team_list = get_other_teams(team)

    if season == '2017-18':
        template = 'stats_team_pages/simulated_team_page.html'
        game_dict = get_simulated_games(team)
    else:
        template = 'stats_team_pages/team_page.html'
        game_dict = get_games(team)

    context = {'team': team,
               'team_logo': team_logo,
               'team_name': team_name,
               'team_list': team_list,
               'game_dict': game_dict,
               'season': season
               }

    return render(request, template, context)
