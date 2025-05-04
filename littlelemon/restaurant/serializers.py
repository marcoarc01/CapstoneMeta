from rest_framework import serializers
from .models import BookingTable, MenuTable

class BookingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'

class MenuTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = '__all__'