from chartjs.views.lines import BaseLineChartView
from django.shortcuts import render
from django.views.generic import TemplateView

from stats.create_graph_data import top_ten_wlr, top_ten_points, top_ten_rebounds, top_ten_assists
from stats.game_stats_data import create_data
from stats.all_team_data import create_team_data
from stats.standing_data import create_standing_data

from stats.team_comparisons import create_divisions_data


def main_page(request):
    return render(request, 'stats/main_page.html')


def box_score(request):
    game_id = request.GET['gameID']
    data = create_data(game_id)
    headers = data[0]
    rows1 = data[1]
    rows2 = data[2]
    team1_name = data[3]
    team2_name = data[4]
    team1 = data[5]
    team2 = data[6]

    context = {'headers': headers,
               'rows1': rows1,
               'rows2': rows2,
               'team1_name': team1_name,
               'team2_name': team2_name,
               'team1': team1,
               'team2': team2}

    return render(request, 'stats/box_score.html', context)


def all_team_stats(request):
    sort = request.GET.get('sort')
    data = create_team_data(sort)
    headers = data['headers']
    rows = data['rows']

    context = {'headers': headers,
               'rows': rows,
               }

    return render(request, 'stats/all_team_stats.html', context)


def standing(request, season):
    data = create_standing_data(season)
    headers = data[0]
    rows = data[1]

    if season == '2017-18':
        template = 'stats/simulated_standing.html'
    else:
        template = 'stats/standing.html'

    context = {'headers': headers,
               'rows': rows,
               'season': season
               }

    return render(request, template, context)


class GetData:
    def __init__(self):
        data = top_ten_wlr()
        self.labels = [single_team[0] for single_team in data]
        self.wlr = [single_team[1] for single_team in data]

        data2 = top_ten_points()
        self.names = [single_team[0] for single_team in data2]
        self.points = [single_team[1] for single_team in data2]

        data3 = top_ten_rebounds()
        self.teams = [single_team[0] for single_team in data3]
        self.rebounds = [single_team[1] for single_team in data3]

        data4 = top_ten_assists()
        self.abb = [single_team[0] for single_team in data4]
        self.assists = [single_team[1] for single_team in data4]


class WlrChart(BaseLineChartView, GetData):
    def get_labels(self):
        """Return 10 top teams for the x-axis."""
        GetData.__init__(self)
        return self.labels[:10]

    def get_providers(self):
        """Return the name of the category."""
        return ["Win - Loss Ratio"]

    def get_data(self):
        """Return 4 data sets to plot."""
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
        """Return 4 data sets to plot."""
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
        """Return 4 data sets to plot."""
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
        """Return 4 data sets to plot."""
        return [self.assists[:10]]


assists_chart = TemplateView.as_view(template_name='stats/stats_graph.html')
bar_assists_chart = AssistsChart.as_view()


def team_comparisons(request):
    compare = request.GET.get('compare')
    data = create_divisions_data(compare)
    west_divisions = data[0]
    east_divisions = data[1]
    all_teams = data[2]
    categories1 = data[3]
    categories2 = data[4]
    abbreviations = data[5]
    team1 = {data[6]: 'images/' + data[6] + '.png'}
    team2 = {data[7]: 'images/' + data[7] + '.png'}

    context = {'west_divisions': west_divisions,
               'east_divisions': east_divisions,
               'all_teams': all_teams,
               'categories1': categories1,
               'categories2': categories2,
               'abbreviations': abbreviations,
               'team1': team1,
               'team2': team2
               }

    return render(request, 'stats/team_comparisons.html', context)


def stats_graph(request):
    context = {'wlr_chart': bar_wlr_chart,
               'points_chart': bar_points_chart,
               'bar_rebounds_chart': bar_rebounds_chart,
               'bar_assists_chart': bar_assists_chart}

    return render(request, 'stats/stats_graph.html', context)
