from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Corporation
from .serializers.common import CorporationSerializer
from .serializers.populated import PopulatedCorporationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Path: /corporations/
# Methods: GET, POST
class CorporationListCreateView(ListCreateAPIView):
  queryset = Corporation.objects.all()
  serializer_class = CorporationSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Path: /corporations/:pk/
# Methods: GET, PUT, PATCH, DELETE
class CorporationDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Corporation.objects.all()
  permission_classes = [IsAuthenticatedOrReadOnly]

  def get_serializer_class(self):
    if self.request.method == 'PUT':
      return CorporationSerializer
    return PopulatedCorporationSerializer
