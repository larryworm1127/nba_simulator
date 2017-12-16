from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page),
    url(r'^all_team_statistics/$', views.all_team_stats),
    url(r'^boxscore/$', views.boxscore),
    url(r'^view_standing/(?P<season>[0-9-]+)$', views.standing),
]
