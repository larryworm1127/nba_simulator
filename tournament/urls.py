from django.conf.urls import url
from tournament import views

urlpatterns = [
    url(r'^api/(?P<season>[0-9-]+)$', views.tournament, name='api'),
    url(r'^bracket/$', views.bracket),
    url(r'^bracket/(?P<season>[0-9-]+)$', views.bracket, name='tournament_bracket'),
    url(r'^bracket/simulate_playoff$', views.simulate_playoff),
    url(r'^bracket/simulate_season$', views.simulate_season)
]
