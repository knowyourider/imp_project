from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # url('admin/', admin.site.urls),
    path('ancillary/', include('ancillary.urls', namespace='ancillary')),
    path('', include('core.urls', namespace='core')),
    path('map/', include('map.urls', namespace='map')),
    path('special/', include('special.urls', namespace='special')),
    path('stories/', include('stories.urls', namespace='stories')),
    path('supporting/', include('supporting.urls', namespace='supporting')),
    path('themes/', include('themes.urls', namespace='themes')),
]

if settings.DEBUG:
	urlpatterns.append( path('admin/', admin.site.urls))
