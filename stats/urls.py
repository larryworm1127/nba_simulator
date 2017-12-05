from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all_team_statistics/$', views.all_team_stats),
    url(r'^boxscore/$', views.boxscore)
]
