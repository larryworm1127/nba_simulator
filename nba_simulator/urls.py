from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('stats.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^tournament/', include('tournament.urls')),
    url(r'^stats/', include('stats.urls')),
    url(r'^season_games/', include('season_games.urls')),
]
