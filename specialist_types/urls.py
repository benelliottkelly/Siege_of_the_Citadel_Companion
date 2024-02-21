from django.urls import path
from .views import SpecialistTypeListCreateView, SpecialistTypeDetailView

urlpatterns = [
  path('', SpecialistTypeListCreateView.as_view()), # /specialist_types/
  path('<int:pk>/', SpecialistTypeDetailView.as_view()) # /specialist_typese/:pk/
]