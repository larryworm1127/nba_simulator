from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^line_chart_json$', views.line_chart_json, name='line_chart_json'),
]
