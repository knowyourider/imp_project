from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.HomeTemplateView.as_view(), name='home'),
    url(r'^home/intro/$', views.IntroTemplateView.as_view(), name='home_intro'),
    url(r'^team/$', views.TeamHomeTemplateView.as_view(), name='team_home'),
    url(r'^sitemap/$', views.SitemapTemplateView.as_view(), name='sitemap'),
]
