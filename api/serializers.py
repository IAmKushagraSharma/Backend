from rest_framework import serializers
from api import models


class SatelliteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SatelliteInfo
        fields = ['Name']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sensor
        fields = ['SensorName']



class SensorallSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sensor
        fields = '__all__'


