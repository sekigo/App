from django.shortcuts import render
from rest_framework import generics, status, viewsets, mixins
from rest_framework.response import Response
from .models import Sportsman, Category
from .serializer import SportSerializer
from rest_framework.decorators  import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

class SportViewSet(viewsets.ModelViewSet):
    queryset = Sportsman.objects.all()
    serializer_class = SportSerializer


    def get_queryset(self):
        return Sportsman.objects.all()[:3]


    @action(methods =['get'], detail = True)
    def category(self, request, pk = None):
        cats = Category.objects.get(pk=pk)
        return Response({"cats": cats.name})

    
# class SportAPIList(generics.ListCreateAPIView): 
#     queryset = Sportsman.objects.all()
#     serializer_class = SportSerializer
    


# class SportAPIUpdate(generics.UpdateAPIView):
#     queryset = Sportsman.objects.all()
#     serializer_class = SportSerializer


# class SportAPIDetail(generics.RetrieveUpdateDestroyAPIView ):
#     queryset = Sportsman.objects.all()
#     serializer_class = SportSerializer





