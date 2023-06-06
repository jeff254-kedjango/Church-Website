from rest_framework import serializers
from .models import Sermons, SermonShorts


class SermonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermons
        fields = '__all__'


class SermonShortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SermonShorts
        fields = '__all__'