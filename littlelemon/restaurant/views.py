from django.shortcuts import render
from .serializers import BookingTableSerializer, MenuTableSerializer
from rest_framework import generics, viewsets
from .models import MenuTable, BookingTable
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
     return Response({"message":"This view is protected"})

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer
    

class BookingView(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer

class SingleBookingView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer

