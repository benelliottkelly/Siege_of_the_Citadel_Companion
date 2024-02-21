from .common import LevelSerializer
from entrance_points.serializers.common import EntrancePointSerializer
from events.serializers.common import EventSerializer
from dark_legion_resources.serializers.common import DarkLegionResourceSerializer

class PopulatedLevelSerializer(LevelSerializer):
  dark_legion_entrance_points = EntrancePointSerializer(many=True)
  potential_events = EventSerializer(many=True)
  dark_legion_resources = DarkLegionResourceSerializer(many=True)