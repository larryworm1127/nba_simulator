from django.shortcuts import render
from .models import Bar_graph
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 10 top teams for the x-axis."""
        return ["GSW", "CLC"]

    def get_providers(self):
        """Return names of the category."""
        return ["Win - Loss Ratio"]

    def get_data(self):
        """Return 4 data sets to plot."""

        return [[0.81, 0.72, 0.68]]


line_chart = TemplateView.as_view(template_name='index.html')
line_chart_json = LineChartJSONView.as_view()


class LineChartJSONView2(BaseLineChartView):
    def get_labels(self):
        """Return 10 top teams for the x-axis."""
        return ["GSW", "CLC"]

    def get_providers(self):
        """Return names of the category."""
        return ["Points Per Game"]

    def get_data(self):
        """Return 4 data sets to plot."""
        return [[0.81, 0.72, 0.68]]


line_chart2 = TemplateView.as_view(template_name='index.html')
line_chart_json2 = LineChartJSONView2.as_view()


class LineChartJSONView3(BaseLineChartView):
    def get_labels(self):
        """Return 10 top teams for the x-axis."""
        return ["GSW", "CLC"]

    def get_providers(self):
        """Return names of the category."""
        return ["Rebounds Per Game"]

    def get_data(self):
        """Return 4 data sets to plot."""
        return [[0.81, 0.72, 0.68]]


line_chart3 = TemplateView.as_view(template_name='index.html')
line_chart_json3 = LineChartJSONView3.as_view()


class LineChartJSONView4(BaseLineChartView):
    def get_labels(self):
        """Return 10 top teams for the x-axis."""
        return ["GSW", "CLC"]

    def get_providers(self):
        """Return names of the category."""
        return ["Assists Per Game"]

    def get_data(self):
        """Return 4 data sets to plot."""
        return [[0.81, 0.72, 0.68]]


line_chart4 = TemplateView.as_view(template_name='index.html')
line_chart_json4 = LineChartJSONView4.as_view()


def index(request):
    bar_title = Bar_graph.bgraph_title
    return render(request, 'bar_graphs/index.html', {'bar_title': bar_title, 'line_chart_json': line_chart_json,
                                                     'line_chart_json2': line_chart_json2,
                                                     'line_chart_json3': line_chart_json3,
                                                     'line_chart_json4': line_chart_json4})
