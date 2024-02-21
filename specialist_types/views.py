from rest_framework.generics import CreateAPIView
from .models import SpecialistType
from serializers.common import SpecialistTypeSerializer
from serializers.populated import PopulatedSpecialistTypeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Path: /specialist_types/
# Methods: GET, POST
class SpecialistTypesListCreateView(CreateAPIView):
  queryset = SpecialistType.objects.all()
  serializer_class = SpecialistTypeSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]