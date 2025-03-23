from rest_framework import serializers
from visualization.models import DataPoint

class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = '__all__'