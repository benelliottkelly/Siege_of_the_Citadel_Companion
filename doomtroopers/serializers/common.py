from rest_framework import serializers
from ..models import Doomtrooper

class DoomtrooperSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doomtrooper
    fields = '__all__'