from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<team>[A-Z-]+)$', views.season_games)
]