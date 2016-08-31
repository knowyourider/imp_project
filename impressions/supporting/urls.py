from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^context/$', views.ContextListView.as_view(), name='context_list'),
    url(r'^context/(?P<pk>[0-9]+)/$', views.ContextDetailView.as_view(), name='context_detail_pk'),
    url(r'^context/(?P<slug>\S+)/$', views.ContextDetailView.as_view(), name='context_detail'),

    url(r'^evidenceitem/$', views.EvidenceItemListView.as_view(), name='evidenceitem_list'),
    url(r'^evidenceitem/(?P<pk>[0-9]+)/$', views.EvidenceItemDetailView.as_view(), 
    	name='evidenceitem_detail_pk'),
    url(r'^evidenceitem/(?P<slug>\S+)/$', views.EvidenceItemDetailView.as_view(), 
    	name='evidenceitem_detail'),

    url(r'^fastfact/(?P<pk>[0-9]+)/$', views.FastFactDetailView.as_view(), 
    	name='fastfact_detail_pk'),
    url(r'^fastfact/(?P<slug>\S+)/$', views.FastFactDetailView.as_view(), 
    	name='fastfact_detail'),
    
    url(r'^person/$', views.PersonListView.as_view(), name='person_list'),
    url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view(), name='person_detail_pk'),
    url(r'^person/(?P<slug>\S+)/$', views.PersonDetailView.as_view(), name='person_detail'),

    url(r'^special/$', views.SpecialListView.as_view(), name='special_list'),
    url(r'^special/(?P<slug>\S+)/$', views.SpecialDetailView.as_view(), name='special_detail'),
]
