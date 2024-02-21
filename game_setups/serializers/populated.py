from .common import GameSetupSerializer
from users.serializers.common import UserSerializer
from levels.serializers.common import LevelSerializer
from corporations.serializers.common import CorporationSerializer

class PopulatedGameSetupSerializer(GameSetupSerializer):
  owner = UserSerializer
  mission = LevelSerializer(many=True)
  corporations = CorporationSerializer(many=True)