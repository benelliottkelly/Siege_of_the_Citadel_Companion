from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import DarkLegion
from .serializers.common import DarkLegionSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Path: /dark_legion/
# Methods: GET, POST
class DarkLegionCreateAPIView(ListCreateAPIView):
  queryset = DarkLegion.objects.all()
  serializer_class = DarkLegionSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Path: /dark_legion/:pk/
# Methods: GET, PUt, PATCH, DELETE
class DarkLegionDetailView(RetrieveUpdateDestroyAPIView):
  queryset = DarkLegion.objects.all()
  serializer_class = DarkLegionSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
