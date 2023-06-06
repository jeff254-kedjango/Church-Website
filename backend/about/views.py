from .models import About,Dailydevotion,Notices
from .serializers import AboutSerializer,DailydevotionSerializer,NoticesSerializer
from rest_framework import generics


class AboutList(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class DailyDevotionList(generics.ListCreateAPIView):
    queryset = Dailydevotion.objects.all()
    serializer_class = DailydevotionSerializer

class DailyDevotionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dailydevotion.objects.all()
    serializer_class = DailydevotionSerializer

class NoticesList(generics.ListCreateAPIView):
    queryset = Notices.objects.all()
    serializer_class = NoticesSerializer

class NoticesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notices.objects.all()
    serializer_class = NoticesSerializer