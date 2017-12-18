from django.conf.urls import url
from tournament import views

urlpatterns = [
    url(r'^api/(?P<season>[0-9-]+)$', views.tournament),
    url(r'^bracket/$', views.bracket),
    url(r'^bracket/(?P<season>[0-9-]+)$', views.bracket),
    url(r'^bracket/simulate_playoff$', views.simulate_playoff),
    url(r'^bracket/simulate_season$', views.simulate_season)
]
