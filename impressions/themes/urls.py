from django.urls import path
from . import views

app_name="themes"

urlpatterns = [
    path('', views.ThemeListView.as_view(), name='theme_list'),
    path('<slug:slug>/', views.ThemeDetailView.as_view(), name='theme_detail'),
]
