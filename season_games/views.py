from django.shortcuts import render
from season_games.create_team_page_data import get_team_from_abb, get_other_teams, get_games, get_simulated_games


def season_games(request, team, season):
    team_logo = "images/" + team + ".png"
    team_name = get_team_from_abb(team)
    team_list = get_other_teams(team)

    if season == '2018':
        template = 'season_games/simulated_team_page.html'
        game_dict = get_simulated_games(team)
        standing_url = '/stats/view_simulated_standing'
    else:
        template = 'season_games/team_page.html'
        game_dict = get_games(team)
        standing_url = '/stats/view_wins_and_losses'

    return render(request, template,
                  {'team': team,
                   'team_logo': team_logo,
                   'team_name': team_name,
                   'team_list': team_list,
                   'game_dict': game_dict,
                   'standing_url': standing_url
                   })
