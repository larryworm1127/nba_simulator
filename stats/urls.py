from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='main_page'),
    url(r'^all_team_stats/$', views.all_team_stats, name='all_team_stats'),
    url(r'^box_score/$', views.box_score, name='box_score'),
    url(r'^standing/(?P<season>[0-9-]+)$', views.standing, name='standing'),
    url(r'^graphs/$', views.stats_graph, name='graphs'),
    url(r'^graphs/bar_wlr_chart', views.bar_wlr_chart, name='bar_wlr_chart'),
    url(r'^graphs/bar_points_chart', views.bar_points_chart, name='bar_points_chart'),
    url(r'^graphs/bar_rebounds_chart', views.bar_rebounds_chart, name='bar_rebounds_chart'),
    url(r'^graphs/bar_assists_chart', views.bar_assists_chart, name='bar_assists_chart'),
    url(r'^team_comparisons/$', views.team_comparisons, name='team_comparisons'),
    url(r'^(?P<season>[0-9-]+)/(?P<team>[A-Z-]+)$', views.season_games, name='stats_team_pages')

]
