from rest_framework import serializers
from ..models import BattleReport

class BattleReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = BattleReport
    fields = '__all__'