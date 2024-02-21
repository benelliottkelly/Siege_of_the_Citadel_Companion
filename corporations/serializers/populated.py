from .common import CorporationSerializer
from doomtroopers.serializers.common import DoomtrooperSerializer

class PopulatedCorporationSerializer(CorporationSerializer):
  doomtroopers = DoomtrooperSerializer(many=True)