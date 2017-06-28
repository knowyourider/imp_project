from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^ancillary/', include('ancillary.urls', namespace='ancillary')),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^map/', include('map.urls', namespace='map')),
    url(r'^special/', include('special.urls', namespace='special')),
    url(r'^stories/', include('stories.urls', namespace='stories')),
    url(r'^supporting/', include('supporting.urls', namespace='supporting')),
    url(r'^themes/', include('themes.urls', namespace='themes')),
]

if settings.DEBUG:
	urlpatterns.append( url(r'^admin/', admin.site.urls))
