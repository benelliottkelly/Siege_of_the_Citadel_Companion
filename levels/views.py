from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Level
from .serializers.common import LevelSerializer
from .serializers.populated import PopulatedLevelSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Path: /levels/
# Methods: GET, POST
class LevelListCreateView(ListCreateAPIView):
  queryset = Level.objects.all().prefetch_related('dark_legion_entrance_points', 'potential_events', 'dark_legion_resources')
  serializer_class = LevelSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Path: /levels/:pk/
# Methods: GET, PUT, PATCH, DELETE
class LevelDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Level.objects.all().prefetch_related('dark_legion_entrance_points', 'potential_events', 'dark_legion_resources')
  permission_classes = [IsAuthenticatedOrReadOnly]

  def get_serializer_class(self):
    if self.request.method == 'PUT':
      return LevelSerializer
    return PopulatedLevelSerializer
