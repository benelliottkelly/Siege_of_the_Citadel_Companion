from rest_framework import serializers
from ..models import GameSetup

class GameSetupSerializer(serializers.ModelSerializer):
  class Meta:
    model = GameSetup
    fields = '__all__'