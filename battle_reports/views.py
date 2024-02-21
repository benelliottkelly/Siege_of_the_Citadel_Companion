from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import BattleReport
from .serializers.common import BattleReportSerializer
from .serializers.populated import PopulatedBattleReportSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from lib.views import OwnerListCreateView
from lib.permissions import IsOwnerOrReadOnly

# Path: /battle_reports/
# Methods: GET, POST
class BattleReportListCreateView(OwnerListCreateView):
  queryset = BattleReport.objects.all()
  serializer_class = BattleReportSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

# Path: /battle_reports/:pk/
# Methods: GET, PUT, PATCH, DELETE
class BattleReportDetailView(RetrieveUpdateDestroyAPIView):
  queryset = BattleReport.objects.all().select_related('owner')
  permission_classes = [IsOwnerOrReadOnly]
  
  def get_serializer_class(self):
    if self.request.method == 'PUT':
      return BattleReportSerializer
    return PopulatedBattleReportSerializer
