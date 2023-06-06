from rest_framework import serializers
from .models import Books, Merchandise

class BooksSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Books
        fields = '__all__'


class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = '__all__'