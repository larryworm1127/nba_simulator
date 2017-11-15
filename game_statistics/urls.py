from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^boxscore_example/$', views.boxscore_example)
]
