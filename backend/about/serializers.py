from rest_framework import serializers
from .models import About,Dailydevotion,Notices

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class DailydevotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dailydevotion
        fields = '__all__'


class NoticesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = '__all__'