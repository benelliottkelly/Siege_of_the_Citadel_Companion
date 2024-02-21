from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import EntrancePoint
from .serializers.common import EntrancePointSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Path: /entrance_points/
# Methods: GET, POST
class EntrancePointCreateAPIView(ListCreateAPIView):
  queryset = EntrancePoint.objects.all()
  serializer_class = EntrancePointSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Path: /entrance_points/:pk/
# Methods: GET, PUT, PATCH, DELETE
class EntrancePointDetailView(RetrieveUpdateDestroyAPIView):
  queryset = EntrancePoint.objects.all()
  serializer_class = EntrancePointSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
