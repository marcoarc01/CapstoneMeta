from django.shortcuts import render
from .serializers import BookingTableSerializer, MenuTableSerializer
from rest_framework import generics, viewsets
from .models import MenuTable, BookingTable

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer
    

class BookingView(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer

class SingleBookingView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer

