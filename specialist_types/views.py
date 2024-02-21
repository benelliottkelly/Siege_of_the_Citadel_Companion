from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import SpecialistType
from .serializers.common import SpecialistTypeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Path: /specialist_types/
# Methods: GET, POST
class SpecialistTypeListCreateView(CreateAPIView):
  queryset = SpecialistType.objects.all()
  serializer_class = SpecialistTypeSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Path: /specialist_types/:pk/
# Methods: GET, PUT, PATCH, DELETE
class SpecialistTypeDetailView(RetrieveUpdateDestroyAPIView):
  queryset = SpecialistType.objects.all()
  serializer_class = SpecialistTypeSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]