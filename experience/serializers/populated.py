from .common import ExperienceSerializer
from battle_reports.serializers.common import BattleReportSerializer
from corporations.serializers.common import CorporationSerializer

class PopulatedExperienceSerializer(ExperienceSerializer):
  battle_report = BattleReportSerializer(many=True)
  corporation = CorporationSerializer(many=True)