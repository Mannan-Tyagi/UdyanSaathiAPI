# serializers.py
from rest_framework import serializers
from .models import pollutionModel

class PollutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = pollutionModel
        fields = '__all__'
