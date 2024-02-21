from django.urls import path
from .views import GameSetupListCreateView, GameSetupDetailView

urlpatterns = [
  path('', GameSetupListCreateView.as_view()), # /game_setups/
  path('<int:pk>/', GameSetupDetailView.as_view()) # /games_setups/:pk/
]