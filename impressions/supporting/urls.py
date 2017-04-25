from django.conf.urls import url
from . import views


urlpatterns = [
    # aka Backgrounds
    url(r'^context/$', views.ContextListView.as_view(paginate_by=21), name='context_list'),
    url(r'^context/(?P<pk>[0-9]+)/$', views.ContextDetailView.as_view(), \
        name='context_detail_pk'),
    url(r'^context/(?P<slug>\S+)/$', views.ContextDetailView.as_view(), \
        name='context_detail'),

    url(r'^evidenceitem/$', views.EvidenceItemListView.as_view(paginate_by=20), 
        name='evidenceitem_list'), 
    # only for team lists - still used?
    url(r'^evidenceitem/(?P<pk>[0-9]+)/$', views.EvidenceItemDetailView.as_view(), 
        name='evidenceitem_detail_pk'),
    # supports ajax for both artifact and document pages
    url(r'^evidence/(?P<slug>\S+)/(?P<page_suffix>\S+)/$', \
        views.evidence_page, name='evidence_page_detail'),   
    # is_document_oriented evidenceitems need separte view that supplies 1st page
    url(r'^document/(?P<slug>\S+)/$', views.DocumentDetailView.as_view(), 
      name='document_detail'),
    # non is_document_oriented evidenceitems (artifacts) default to no page info
    url(r'^artifact/(?P<slug>\S+)/$', views.ArtifactDetailView.as_view(), 
      name='artifact_detail'),

    # aka In Briefs
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
