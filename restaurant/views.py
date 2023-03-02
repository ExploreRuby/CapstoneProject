from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu,Booking
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
    return render(request,'index1.html',{})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset= Menu.objects.all()
    serializer_class = MenuSerializer 

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        items = Booking.objects.all()
        serialized_item = BookingSerializer(items,many=True)
        return Response({"data": serialized_item.data})
    def post(Self,request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success","data": serializer.data})




