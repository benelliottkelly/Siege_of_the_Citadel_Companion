from django.urls import path
from .views import SpecialistTypesListCreateView

urlpatterns = [
  path('', SpecialistTypesListCreateView.as_view()), # /specialist_types/
]