from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('data_display.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^data_display/', include('data_display.urls')),
    url(r'^tournament/', include('tournament.urls')),
    url(r'^stats/', include('stats.urls'))
]
