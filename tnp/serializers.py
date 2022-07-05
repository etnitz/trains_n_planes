from dataclasses import fields
from rest_framework import serializers
from .models import Train

class TrainSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Train
        fields = ('id', 'name', 'power_type', 'builder', 'year', 'country', 'description', 'photo_url')

