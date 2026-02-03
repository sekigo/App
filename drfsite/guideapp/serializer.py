from rest_framework import serializers
from .models import Sportsman

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sportsman
        fields = ('name', 'cat_id')