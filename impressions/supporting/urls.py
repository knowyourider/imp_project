from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^context/$', views.ContextListView.as_view(paginate_by=21), name='context_list'),
    url(r'^context/(?P<pk>[0-9]+)/$', views.ContextDetailView.as_view(), \
        name='context_detail_pk'),
    url(r'^context/(?P<slug>\S+)/$', views.ContextDetailView.as_view(), \
        name='context_detail'),

    url(r'^evidenceitem/$', views.EvidenceItemListView.as_view(paginate_by=21), name='evidenceitem_list'),

    # test what's being called -- comment this out
    # url(r'^evidenceitem/(?P<slug>\S+)/(?P<page_suffix>\S+)/$', \
    #     views.evidenceitem_detail, name='evidenceitem_detail'),   
    
    # only for team lists
    url(r'^evidenceitem/(?P<pk>[0-9]+)/$', views.EvidenceItemDetailView.as_view(), 
        name='evidenceitem_detail_pk'),

    # will be obsolete
    url(r'^evidenceitem/(?P<slug>\S+)/$', views.evidenceitem_detail, name='evidenceitem_detail'),

    # not used -- using artifact or document instead    
    # url(r'^evidenceitem/(?P<slug>\S+)/$', views.EvidenceItemDetailView.as_view(), 
    #   name='evidenceitem_detail'),

    # works
    url(r'^document/(?P<slug>\S+)/(?P<page_suffix>\S+)/$', \
        views.DocumentDetailView.as_view(), name='document_page_detail'),   
    # new - works
    url(r'^document/(?P<slug>\S+)/$', views.DocumentDetailView.as_view(), 
      name='document_detail'),
    # new and testing
    url(r'^artifact/(?P<slug>\S+)/(?P<page_suffix>\S+)/$', \
        views.ArtifactPageDetailView.as_view(), name='artifact_page_detail'),   
    # check, this is new and working:
    url(r'^artifact/(?P<slug>\S+)/$', views.ArtifactDetailView.as_view(), 
      name='artifact_detail'),


    url(r'^fastfact/(?P<pk>[0-9]+)/$', views.FastFactDetailView.as_view(), 
        name='fastfact_detail_pk'),
    url(r'^fastfact/(?P<slug>\S+)/$', views.FastFactDetailView.as_view(), 
        name='fastfact_detail'),
    
    url(r'^person/$', views.PersonListView.as_view(), name='person_list'),
    url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view(), name='person_detail_pk'),
    url(r'^person/(?P<slug>\S+)/$', views.PersonDetailView.as_view(), name='person_detail'),

    # -- team pages  
    url(r'^team/evidenceitem/$', views.EvidenceItemListView.as_view(template_name=\
        "supporting/team_item_list.html"), name='team_evidenceitem_list'),
    url(r'^team/person/$', views.PersonListView.as_view(template_name=\
        "supporting/team_item_list.html"), name='team_person_list'),
    url(r'^team/context/$', views.ContextListView.as_view(template_name=\
        "supporting/team_item_list.html"), name='team_context_list'),
    # url for special list in special/urls.py
    url(r'^team/$', views.TeamTemplateView.as_view(), name='team_type_list'),
]
