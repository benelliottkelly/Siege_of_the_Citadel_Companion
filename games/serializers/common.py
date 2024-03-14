from rest_framework import serializers
from ..models import Game

class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = '__all__'

class CreateGameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = '__all__'

  def validate(self, data):
    # make sure the number of corporations added is equal to the number of players selected
    if (len(data.get('corporations')) != data.get('number_of_players')):
      raise serializers.ValidationError({'data': ['The number of players must match the number of Corporations selected']})
    else:
      return data