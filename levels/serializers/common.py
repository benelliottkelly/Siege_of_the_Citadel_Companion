from rest_framework import serializers
from ..models import Level

class LevelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Level
    fields = '__all__'

    def validate_map(self, value):
        """
        Ensure tiles length == width * height
        """
        width = value.get("width")
        height = value.get("height")
        tiles = value.get("tiles")

        if width is None or height is None or tiles is None:
            raise serializers.ValidationError(
                "Map must include width, height, and tiles."
            )

        if len(tiles) != width * height:
            raise serializers.ValidationError(
                f"Number of tiles length must equal width * height."
            )

        return value