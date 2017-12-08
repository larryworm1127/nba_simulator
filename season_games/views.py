from django.shortcuts import render
from os.path import join


def season_games(request, team):
	team_logo = "images/" + team + ".png"
	return render(request, 'season_games/team_page.html', {'team': team, 'team_logo': team_logo})