from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^context/$', views.ContextListView.as_view(), name='context_list'),
    url(r'^context/(?P<slug>\S+)/$', views.ContextDetailView.as_view(), name='context_detail'),
    url(r'^evidenceitem/$', views.EvidenceItemListView.as_view(), name='evidenceitem_list'),
    url(r'^evidenceitem/(?P<slug>\S+)/$', views.EvidenceItemDetailView.as_view(), name='evidenceitem_detail'),
    url(r'^fastfact/(?P<slug>\S+)/$', views.FastFactDetailView.as_view(), name='fastfact_detail'),
    url(r'^person/$', views.PersonListView.as_view(), name='person_list'),
    url(r'^person/(?P<slug>\S+)/$', views.PersonDetailView.as_view(), name='person_detail'),
]
