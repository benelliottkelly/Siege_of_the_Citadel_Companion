from django.urls import path
from .views import BattleReportListCreateView, BattleReportDetailView

urlpatterns = [
  path('', BattleReportListCreateView.as_view()), # /battle_reports/
  path('<int:pk>/', BattleReportDetailView.as_view()) # /battle_reports/:pk/
]