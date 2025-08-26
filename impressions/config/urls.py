from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url('admin/', admin.site.urls),
    path('ancillary/', include('ancillary.urls', namespace='ancillary')),
    path('', include('core.urls', namespace='core')),
    path('map/', include('map.urls', namespace='map')),
    path('special/', include('special.urls', namespace='special')),
    path('stories/', include('stories.urls', namespace='stories')),
    path('supporting/', include('supporting.urls', namespace='supporting')),
    path('themes/', include('themes.urls', namespace='themes')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Also ensure static files are served
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
