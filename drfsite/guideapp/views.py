from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .models import Sportsman
from .serializer import SportSerializer
from rest_framework.decorators  import api_view
from rest_framework.views import APIView







class SportViewSet(viewsets.ModelViewSet):
    queryset = Sportsman.objects.all()
    serializer_class = SportSerializer



# class SportAPIList(generics.ListCreateAPIView): 
#     queryset = Sportsman.objects.all()
#     serializer_class = SportSerializer
    


# class SportAPIUpdate(generics.UpdateAPIView):
#     queryset = Sportsman.objects.all()
#     serializer_class = SportSerializer


# class SportAPIDetail(generics.RetrieveUpdateDestroyAPIView ):
#     queryset = Sportsman.objects.all()
#     serializer_class = SportSerializer





