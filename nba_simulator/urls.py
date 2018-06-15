from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('stats.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^stats_brackets/', include('stats_brackets.urls')),
    url(r'^stats/', include('stats.urls')),
]
