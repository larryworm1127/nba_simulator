from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page),
    url(r'^all_team_statistics/$', views.all_team_stats),
    url(r'^box_score/$', views.box_score),
    url(r'^view_standing/(?P<season>[0-9-]+)$', views.standing),
    url(r'^graphs/$', views.stats_graph, name='index'),
    url(r'^graphs/bar_wlr_chart', views.bar_wlr_chart, name='bar_wlr_chart'),
    url(r'^graphs/bar_points_chart', views.bar_points_chart, name='bar_points_chart'),
    url(r'^graphs/bar_rebounds_chart', views.bar_rebounds_chart, name='bar_rebounds_chart'),
    url(r'^graphs/bar_assists_chart', views.bar_assists_chart, name='bar_assists_chart'),
    url(r'^view_team_comparisons/$', views.team_comparisons),
]
