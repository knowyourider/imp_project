from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.EvidenceItemListView.as_view(), name='evidenceitem_list'),
    url(r'^(?P<slug>\S+)/$', views.EvidenceItemDetailView.as_view(), name='evidenceitem_detail'),
]
