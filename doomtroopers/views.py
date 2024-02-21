from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Doomtrooper
from .serializers.common import DoomtrooperSerializer
from .serializers.populated import PopulatedDoomtrooperSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from lib.views import OwnerListCreateView
from lib.permissions import IsOwnerOrReadOnly

# Path: /doomtroopers/
# Methods: GET, POST
class DoomtrooperListCreateView(OwnerListCreateView):
  queryset = Doomtrooper.objects.all()
  serializer_class = DoomtrooperSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Path: /doomtroopers/:pk/
# Methods: GET, PUT, PATCH, DELETE
class DoomtrooperDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Doomtrooper.objects.all().select_related('owner')
  permission_classes = [IsOwnerOrReadOnly]

  def get_serializer_class(self):
    if self.request.method == 'PUT':
      return DoomtrooperSerializer
    return PopulatedDoomtrooperSerializer