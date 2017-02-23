"""django19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
# from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^map/', include('map.urls', namespace='map')),
    url(r'^special/', include('special.urls', namespace='special')),
    url(r'^stories/', include('stories.urls', namespace='stories')),
    url(r'^supporting/', include('supporting.urls', namespace='supporting')),
    url(r'^themes/', include('themes.urls', namespace='themes')),
    # url(r'^team/$', views.TeamHomeTemplateView.as_view(), name='team_home'),
]
