# serializers.py
from rest_framework import serializers
from .models import *

class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = graphDataModel
        fields = '__all__'
class PollutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = pollutionModel
        fields = '__all__'
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = stationModel
        fields = '__all__'
class AqiCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AqiCalendarModel
        fields = '__all__'
class Top10CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top10CitiesModel
        fields = '__all__'
class Top10LeastCitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top10LeastCitiesModel
        fields = '__all__'
class TopMetroCitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopMetroCitiesModel
        fields = '__all__'