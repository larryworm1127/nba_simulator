from django.shortcuts import render
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from bar_graphs.create_stats_data import top_ten_wlr, top_ten_points, top_ten_rebounds, top_ten_assists


class GetData(object):
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


wlr_chart = TemplateView.as_view(template_name='index.html')
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


points_chart = TemplateView.as_view(template_name='index.html')
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


rebounds_chart = TemplateView.as_view(template_name='index.html')
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


assists_chart = TemplateView.as_view(template_name='index.html')
bar_assists_chart = AssistsChart.as_view()


def index(request):
    return render(request, 'bar_graphs/index.html',
                  {'wlr_chart': bar_wlr_chart,
                   'points_chart': bar_points_chart,
                   'bar_rebounds_chart': bar_rebounds_chart,
                   'bar_assists_chart': bar_assists_chart})
