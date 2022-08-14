from rest_framework import serializers
from api import models

class SatelliteInfoSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.SatelliteInfo
        fields = '__all__'