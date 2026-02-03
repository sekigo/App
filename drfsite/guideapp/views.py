from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sportsman
from .serializer import SportSerializer

class SportAPIList(generics.ListCreateAPIView):
    queryset = Sportsman.objects.all()
    serializer_class = SportSerializer
class SportAPIView(APIView): # обработка get запросов
    def get(self, request):
        s = Sportsman.objects.all()
        return Response({'posts': SportSerializer(s, many=True).data})


    def post(self, request):
        serializer = SportSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response("Method put is not defined")

        try:
            instance = Sportsman.objects.get(pk = pk)
        except:
            return Response("object not found")
        
        serializer=  SportSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})