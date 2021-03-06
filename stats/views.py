from json import load

from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from constant import SIM_PLAYOFF_PATH, BOXSCORE_HEADER
from constant import TEAM_NAME_DICT, TEAM_DICT, CONF_LIST
from simulator.playoff_simulation import run_whole_simulation
from simulator.season_simulation import init
from .bracket_data import BracketData
from .get_stats import get_all_team_data
from .get_stats import get_boxscore_data
from .get_stats import get_comparison_data
from .get_stats import get_graph_data
from .get_stats import get_team_page_data, get_simulated_games
from .standing_data import create_standing_data


def index(request):
    return render(request, 'stats/index.html')


def box_score(request):
    game_id = request.GET['gameID']
    data = get_boxscore_data(game_id)
    team1_pstats = data[0]
    team2_pstats = data[1]
    team1_name = data[2]
    team2_name = data[3]
    team1_abb = data[4]
    team2_abb = data[5]

    context = {
        'headers': BOXSCORE_HEADER,
        'team1_player_stats': team1_pstats,
        'team2_player_stats': team2_pstats,
        'team1_name': team1_name,
        'team2_name': team2_name,
        'team1_abb': team1_abb,
        'team2_abb': team2_abb
    }

    return render(request, 'stats/box_score.html', context)


def all_team_stats(request):
    sort = request.GET.get('sort')
    data = get_all_team_data(sort)
    headers = data['headers']
    rows = data['rows']

    context = {'headers': headers, 'rows': rows}

    return render(request, 'stats/all_team_stats.html', context)


def standing(request, season):
    data = create_standing_data(season)
    headers = data[0]
    rows = data[1]

    if season == '2017-18':
        template = 'stats/simulated_standing.html'
    else:
        template = 'stats/standing.html'

    context = {
        'headers': headers,
        'rows': rows,
        'season': season
    }

    return render(request, template, context)


class GetData:
    data = get_graph_data()

    labels = [single_team[0] for single_team in data[0]]
    wlr = [single_team[1] for single_team in data[0]]

    names = [single_team[0] for single_team in data[1]]
    points = [single_team[1] for single_team in data[1]]

    teams = [single_team[0] for single_team in data[2]]
    rebounds = [single_team[1] for single_team in data[2]]

    abb = [single_team[0] for single_team in data[3]]
    assists = [single_team[1] for single_team in data[3]]


class WlrChart(BaseLineChartView, GetData):
    def get_labels(self):
        """Return 10 top teams for the x-axis."""
        GetData.__init__(self)
        return self.labels[:10]

    def get_providers(self):
        """Return the name of the category."""
        return ["Win - Loss Ratio"]

    def get_data(self):
        """Return 10 data sets to plot."""
        return [self.wlr[:10]]


wlr_chart = TemplateView.as_view(template_name='stats/stats_graph.html')
bar_wlr_chart = WlrChart.as_view()


class PointsChart(BaseLineChartView, GetData):
    def get_labels(self):
        """Return 10 top teams for the x-axis."""
        GetData.__init__(self)
        return self.names[:10]

    def get_providers(self):
        """Return the name of the category."""
        return ["Points Per Game"]

    def get_data(self):
        """Return 10 data sets to plot."""
        return [self.points[:10]]


points_chart = TemplateView.as_view(template_name='stats/stats_graph.html')
bar_points_chart = PointsChart.as_view()


class ReboundsChart(BaseLineChartView, GetData):
    def get_labels(self):
        """Return 10 top teams for the x-axis."""
        GetData.__init__(self)
        return self.teams[:10]

    def get_providers(self):
        """Return the name of the category."""
        return ["Rebounds Per Game"]

    def get_data(self):
        """Return 10 data sets to plot."""
        return [self.rebounds[:10]]


rebounds_chart = TemplateView.as_view(template_name='stats/stats_graph.html')
bar_rebounds_chart = ReboundsChart.as_view()


class AssistsChart(BaseLineChartView, GetData):
    def get_labels(self):
        """Return 10 top teams for the x-axis."""
        GetData.__init__(self)
        return self.abb[:10]

    def get_providers(self):
        """Return the name of the category."""
        return ["Assists Per Game"]

    def get_data(self):
        """Return 10 data sets to plot."""
        return [self.assists[:10]]


assists_chart = TemplateView.as_view(template_name='stats/stats_graph.html')
bar_assists_chart = AssistsChart.as_view()


def team_comparisons(request):
    compare = request.GET.get('compare')
    data = get_comparison_data(compare)
    west_divisions = data[0]
    east_divisions = data[1]
    all_teams = data[2]
    categories1 = data[3]
    categories2 = data[4]
    team1 = {data[5]: f'images/{data[5]}.png'}
    team2 = {data[6]: f'images/{data[6]}.png'}

    context = {
        'west_divisions': west_divisions,
        'east_divisions': east_divisions,
        'all_teams': all_teams,
        'categories1': categories1,
        'categories2': categories2,
        'team1': team1,
        'team2': team2
    }

    return render(request, 'stats/team_comparisons.html', context)


def stats_graph(request):
    context = {
        'wlr_chart': bar_wlr_chart,
        'points_chart': bar_points_chart,
        'bar_rebounds_chart': bar_rebounds_chart,
        'bar_assists_chart': bar_assists_chart
    }

    return render(request, 'stats/stats_graph.html', context)


def season_games(request, team, season):
    team_logo = f"images/{team}.png"
    team_name = ' '.join(TEAM_NAME_DICT[team])
    team_list = [item for item in TEAM_DICT.values()]
    team_list.remove(team)

    if season == '2017-18':
        template = 'stats_team_pages/simulated_team_page.html'
        game_dict = get_simulated_games(team)
    else:
        template = 'stats_team_pages/team_page.html'
        game_dict = get_team_page_data(team)

    context = {
        'team': team,
        'team_logo': team_logo,
        'team_name': team_name,
        'team_list': team_list,
        'game_dict': game_dict,
        'season': season
    }

    return render(request, template, context)


class Tournament(APIView):
    def get(self, request, format=None):
        data = {'key', 'value'}
        return Response(data)


# @api_view(['GET', 'POST'])
@csrf_exempt
def tournament(request, season):
    data = None
    if season == "2017-18":
        with open(SIM_PLAYOFF_PATH, 'r+') as playoff_file:
            data = load(playoff_file)

    elif season == "2016-17":
        bracket_data = BracketData()

        bracket_data.create_playoff_data()
        data = bracket_data.final_data

    return JsonResponse(data)


def bracket(request, season):
    east_teams = {team: f'images/{team}.png' for team in CONF_LIST['east']}
    west_teams = {team: f'images/{team}.png' for team in CONF_LIST['west']}

    context = {
        'season': season,
        'east_teams': east_teams,
        'west_teams': west_teams,
    }

    return render(request, 'stats_brackets/bracket.html', context)


def simulate_playoff(request):
    return JsonResponse(run_whole_simulation())


def simulate_season(request):
    return JsonResponse(init())
