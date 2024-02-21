from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import GameSetup
from .serializers.common import GameSetupSerializer
from .serializers.populated import PopulatedGameSetupSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from lib.views import OwnerListCreateView
from lib.permissions import IsOwnerOrReadOnly

# Path: /game_setups/
# Methods: GET, POST
class GameSetupListCreateView(OwnerListCreateView):
  queryset = GameSetup.objects.all()
  serializer_class = GameSetupSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Path: /game_setups/:pk/
# Methods: GET, PUT, PATCH, DELETE
class GameSetupDetailView(RetrieveUpdateDestroyAPIView):
  queryset = GameSetup.objects.all()
  permission_classes = [IsOwnerOrReadOnly]

  def get_serializer_class(self):
    if self.request.method == 'PUT':
      return GameSetupSerializer
    return PopulatedGameSetupSerializer
