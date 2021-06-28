from django.urls import path
from . import views

app_name="core"

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    # a place-holder -- not triggered by js because there is no "mobile menu"
    # to be visible or not
    path('home/intro/page/', views.FullIntroTemplateView.as_view(), name='home_intro'),
    # needed to add third element "page" to match the length of all other urls
    # using full vs. ajax
    path('home/ajax/intro/page/', views.IntroTemplateView.as_view(), name='ajax_home_intro'),
    path('team/', views.TeamHomeTemplateView.as_view(), name='team_home'),
    path('sitemap/', views.SitemapTemplateView.as_view(), name='sitemap'),
]
