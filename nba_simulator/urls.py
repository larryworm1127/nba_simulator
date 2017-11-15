"""nba_fans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from more_statistics import views
#from game_statistics import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data_display/', include('data_display.urls')),
    url(r'^tournament/', include('tournament.urls')),
    #url(r'^game_statistics/', include('game_statistics.urls')),
    url(r'^more_statistics/', include('more_statistics.urls'))
]
