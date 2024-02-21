from django.urls import path
from .views import LevelListCreateView, LevelDetailView

urlpatterns = [
  path('', LevelListCreateView.as_view()), # /levels/
  path('<int:pk>/', LevelDetailView.as_view()) # /levels/:pk/
]