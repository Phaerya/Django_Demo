from django.urls import path
from .views import PersonneListView, PersonneDetailView, PersonneCreateView, PersonneUpdateView, PersonneDeleteView
from . import views

urlpatterns = [
    path('', PersonneListView.as_view(), name='personne_list'),
    path('<int:pk>/', PersonneDetailView.as_view(), name='personne_detail'),
    path('new/', PersonneCreateView.as_view(), name='personne_new'),
    path('<int:pk>/edit/', PersonneUpdateView.as_view(), name='personne_edit'),
    path('<int:pk>/delete/', PersonneDeleteView.as_view(), name='personne_delete'),
]
