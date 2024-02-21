from django.urls import path
from .views import CorporationListCreateView, CorporationDetailView

urlpatterns = [
  path('', CorporationListCreateView.as_view()), # /corporations/
  path('<int:pk>/', CorporationDetailView.as_view()) # /corporations/:pk/
]