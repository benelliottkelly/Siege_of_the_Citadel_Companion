from rest_framework import serializers
from ..models import EntrancePoint

class EntrancePointSerializer(serializers.ModelSerializer):
  class Meta:
    model = EntrancePoint
    fields = '__all__'