from .models import Sermons,SermonShorts
from .serializers import SermonsSerializer,SermonShortsSerializer
from rest_framework import generics


class SermonsList(generics.ListCreateAPIView):
    queryset = Sermons.objects.all()
    serializer_class = SermonsSerializer

class SermonsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sermons.objects.all()
    serializer_class = SermonsSerializer

class SermonShortsList(generics.ListCreateAPIView):
    queryset = SermonShorts.objects.all()
    serializer_class = SermonShortsSerializer

class SermonShortsDetail(generics.ListCreateAPIView):
    queryset = SermonShorts.objects.all()
    serializer_class = SermonShortsSerializer
