from .common import BattleReportSerializer
from users.serializers.common import UserSerializer

class PopulatedBattleReportSerializer(BattleReportSerializer):
  owner = UserSerializer(many=True)