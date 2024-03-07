from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Game
from .serializers.common import GameSerializer
from .serializers.populated import PopulatedGameSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from lib.views import OwnerListCreateView
from lib.permissions import IsOwnerOrReadOnly

# Path: /game_setups/
# Methods: GET, POST
class GameListCreateView(OwnerListCreateView):
  queryset = Game.objects.all().select_related('owner').prefetch_related('mission', 'corporations')
  serializer_class = GameSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Path: /game_setups/:pk/
# Methods: GET, PUT, PATCH, DELETE
class GameDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Game.objects.all()
  permission_classes = [IsOwnerOrReadOnly]

  def get_serializer_class(self):
    if self.request.method == 'PUT':
      return GameSerializer
    return PopulatedGameSerializer
