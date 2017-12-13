from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^line_chart_json$', views.line_chart_json, name='line_chart_json'),
    url(r'^line_chart_json2$', views.line_chart_json2, name='line_chart_json2'),
    url(r'^line_chart_json3$', views.line_chart_json3, name='line_chart_json3'),
    url(r'^line_chart_json4$', views.line_chart_json4, name='line_chart_json4'),
]
