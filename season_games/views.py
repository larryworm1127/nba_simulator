from django.shortcuts import render
from season_games.create_team_page_data import get_team_from_abb, get_other_teams, get_games


def season_games(request, team):
    team_logo = "images/" + team + ".png"
    team_name = get_team_from_abb(team)
    team_list = get_other_teams(team)
    game_dict = get_games(team)

    return render(request, 'season_games/team_page.html',
                  {'team': team,
                   'team_logo': team_logo,
                   'team_name': team_name,
                   'team_list': team_list,
                   'game_dict': game_dict
                   })
