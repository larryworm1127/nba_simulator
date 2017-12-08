from django.shortcuts import render
from .models import Bar_graph
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May"]

    def get_providers(self):
        """Return names of data sets."""
        return ["Win - Loss Ratio", "Points Per Game", "Rebounds Per Game", "Assists Per Game"]

    def get_data(self):
        """Return 4 data sets to plot."""

        return [[75, 44, 82, 11, 44],
                [41, 32, 18, 3, 73],
                [87, 21, 44, 3, 50],
                [10, 20, 80, 56, 23]]


line_chart = TemplateView.as_view(template_name='index.html')
line_chart_json = LineChartJSONView.as_view()


def index(request):
    bar_title = Bar_graph.bgraph_title
    return render(request, 'bar_graphs/index.html', {'bar_title': bar_title, 'line_chart_json': line_chart_json})
