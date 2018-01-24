from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<season>[0-9-]+)/(?P<team>[A-Z-]+)$', views.season_games, name='stats_team_pages')
]