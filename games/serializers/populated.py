from .common import GameSerializer
from users.serializers.common import UserSerializer
from levels.serializers.common import LevelSerializer
from corporations.serializers.common import CorporationSerializer

class PopulatedGameSerializer(GameSerializer):
  owner = UserSerializer
  mission = LevelSerializer(many=True)
  corporations = CorporationSerializer(many=True)