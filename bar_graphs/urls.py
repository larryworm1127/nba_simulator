from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bar_wlr_chart', views.bar_wlr_chart, name='bar_wlr_chart'),
    url(r'^bar_points_chart', views.bar_points_chart, name='bar_points_chart'),
    url(r'^bar_rebounds_chart', views.bar_rebounds_chart, name='bar_rebounds_chart'),
    url(r'^bar_assists_chart', views.bar_assists_chart, name='bar_assists_chart'),
]
