from rest_framework import serializers
from ..models import DarkLegion

class DarkLegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = DarkLegion
    fields = '__all__'