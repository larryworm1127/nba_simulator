from django.conf.urls import url
from tournament import views

urlpatterns = [
    url(r'^api/(?P<season>[0-9-]+)$', views.tournament),
    url(r'^bracket/$', views.bracket),
    url(r'^bracket/(?P<season>[0-9-]+)$', views.bracket),
]
