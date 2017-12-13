from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all_team_statistics/$', views.all_team_stats),
    url(r'^boxscore/$', views.boxscore),
    url(r'^view_wins_and_losses/$', views.wins_and_losses),
    url(r'^view_simulated_standing/$', views.simulated_standing)
]
