from django.urls import path
from . import views

app_name="supporting"

urlpatterns = [
    # aka Backgrounds
    path('context/', views.ContextListView.as_view(paginate_by=20), 
        name='context_list'),
    path('context/<int:pk>/', views.ContextDetailView.as_view(), 
        name='context_detail_pk'),
    path('context/<slug:slug>/', views.FullContextDetailView.as_view(), 
        name='context_detail'),
    path('ajax/context/<slug:slug>/', 
        views.ContextDetailView.as_view(), name='ajax_context_detail'),
    #  full screen from swap fullpop
    path('swapfull/context/<slug:slug>/', 
        views.SwapFullContextDetailView.as_view(), name='swapfull_context_detail'),


    # --- EVIDENCE ITEMS --
    path('evidenceitem/', views.EvidenceItemListView.as_view(paginate_by=20), 
        name='evidenceitem_list'), 

    # only for team lists - still used?
    path('evidenceitem/<int:pk>/', views.EvidenceItemDetailView.as_view(), 
        name='evidenceitem_detail_pk'),
    # supports ajax for both artifact and document pages
    # with page suffix - ajax
    path('evidence/<slug:slug>/<page_suffix>/', 
        views.evidence_page, name='evidence_page_detail'),  

    # is_document_oriented evidenceitems need separate view that supplies 1st page
    path('document/<slug:slug>/', views.FullDocumentDetailView.as_view(), 
      name='document_detail'),

    #  ajax 
    path('ajax/document/<slug:slug>/', 
        views.DocumentDetailView.as_view(), name='ajax_document_detail'),

    path('swapfull/document/<slug:slug>/', 
        views.SwapFullDocumentDetailView.as_view(), name='swapfull_document_detail'),

    # non is_document_oriented evidenceitems (artifacts) default to no page info
    path('artifact/<slug:slug>/', views.FullArtifactDetailView.as_view(), 
      name='artifact_detail'),
    #  ajax 
    path('ajax/artifact/<slug:slug>/', 
        views.ArtifactDetailView.as_view(), name='ajax_artifact_detail'),

    path('swapfull/artifact/<slug:slug>/', 
        views.SwapFullArtifactDetailView.as_view(), name='swapfull_artifact_detail'),

    # --- PEOPLE
    path('person/', views.PersonListView.as_view(), name='person_list'),
    path('person/<int:pk>/', views.PersonDetailView.as_view(), 
        name='person_detail_pk'),
    # url('person/<slug:slug>/', views.PersonDetailView.as_view(), 
    #     name='person_detail'),
    # # full screen mobile
    # url('full/person/<slug:slug>/', 
    #     views.FullPersonDetailView.as_view(), name='full_person_detail'),
    path('ajax/person/<slug:slug>/', views.PersonDetailView.as_view(), 
        name='ajax_person_detail'),
    # full screen mobile
    path('person/<slug:slug>/', 
        views.FullPersonDetailView.as_view(), name='person_detail'),
    #  full screen from swap fullpop
    path('swapfull/person/<slug:slug>/', 
        views.SwapFullPersonDetailView.as_view(), name='swapfull_person_detail'),

    # aka In Briefs
    path('fastfact/<int:pk>/', views.FastFactDetailView.as_view(), 
        name='fastfact_detail_pk'),
    path('fastfact/<slug:slug>/', views.FullFastFactDetailView.as_view(), 
        name='fastfact_detail'),
    path('ajax/fastfact/<slug:slug>/', 
        views.FastFactDetailView.as_view(), name='ajax_fastfact_detail'),
    

    # -- team pages  
    path('team/evidenceitem/', views.EvidenceItemListView.as_view(template_name=\
        "supporting/team_item_list.html"), name='team_evidenceitem_list'),
    path('team/person/', views.PersonListView.as_view(template_name=\
        "supporting/team_item_list.html"), name='team_person_list'),
    path('team/context/', views.ContextListView.as_view(template_name=\
        "supporting/team_item_list.html"), name='team_context_list'),
    # url for special list in special/urls.py
    path('team/', views.TeamTemplateView.as_view(), name='team_type_list'),
    path('ziftest/', views.TemplateView.as_view(template_name='zif-test.html'), name='zif-test'),
]
