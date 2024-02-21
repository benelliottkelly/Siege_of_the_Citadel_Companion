from django.urls import path
from .views import DoomtrooperListCreateView, DoomtrooperDetailView

urlpatterns = [
  path('', DoomtrooperListCreateView.as_view()), # /doomtroopers/
  path('<int:pk>/', DoomtrooperDetailView.as_view()) # /doomtroopers/:pk/
]