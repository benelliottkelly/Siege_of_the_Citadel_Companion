from .common import DoomtrooperSerializer
from corporations.serializers.common import CorporationSerializer
from specialist_types.serializers.common import SpecialistTypeSerializer

class PopulatedDoomtrooperSerializer(DoomtrooperSerializer):
  corporation = CorporationSerializer(many=True)
  specialist_type = SpecialistTypeSerializer(many=True)