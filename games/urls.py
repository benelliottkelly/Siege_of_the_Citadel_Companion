from django.urls import path
from .views import GameListCreateView, GameDetailView

urlpatterns = [
  path('', GameListCreateView.as_view()), # /games/
  path('<int:pk>/', GameDetailView.as_view()) # /games/:pk/
]