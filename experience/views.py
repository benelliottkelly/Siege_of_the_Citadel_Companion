from .models import Experience
from .serializers.common import ExperienceSerializer
from .serializers.populated import PopulatedExperienceSerializer
from lib.views import OwnerListCreateView
from lib.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView

# Path: /experience/
# Methods: GET, POST
class ExperienceListCreateView(OwnerListCreateView):
  queryset = Experience.objects.all().select_related('owner', 'battle_report', 'corporation').prefetch_related('doomtroopers_used')
  serializer_class = ExperienceSerializer
  permission_classes = [IsOwnerOrReadOnly]

# Path: /experience/:pk/
#Methods: GET, PUT, PATCH
class ExperienceDetailView(RetrieveUpdateAPIView):
  queryset = Experience.objects.all().select_related('owner', 'battle_report', 'corporation').prefetch_related('doomtroopers_used')
  permission_classes = [IsOwnerOrReadOnly]

  def get_serializer_class(self):
    if self.request.method == 'PUT':
      return ExperienceSerializer
    return PopulatedExperienceSerializer