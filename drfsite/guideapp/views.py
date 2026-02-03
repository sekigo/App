from django.shortcuts import render
from rest_framework import generics
from .models import Sportsman
from .serializer import SportSerializer

class SportAPIView(generics.ListAPIView):
    queryset = Sportsman.objects.all()
    serializer_class = SportSerializer


