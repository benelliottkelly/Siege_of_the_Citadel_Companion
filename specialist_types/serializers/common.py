from rest_framework import serializers
from ..models import SpecialistType

class SpecialistTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = SpecialistType
    fields = '__all__'