from .models import Books,Merchandise
from .serializers import BooksSerializer,MerchandiseSerializer
from rest_framework import generics


class BooksList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class MerchandiseList(generics.ListCreateAPIView):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer

class MerchandiseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer
