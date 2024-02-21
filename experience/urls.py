from django.urls import path
from .views import ExperienceListCreateView, ExperienceDetailView

urlpatterns = [
  path('', ExperienceListCreateView.as_view()), # /api/experience/
  path('<int:pk>/', ExperienceDetailView.as_view()) # /api/experience/:pk/
]