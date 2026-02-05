from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sportsman
from .serializer import SportSerializer
from rest_framework.decorators  import api_view


# class SportAPIList(generics.ListCreateAPIView): # реализует get и post
#     queryset = Sportsman.objects.all()
#     serializer_class = SportSerializer
    
@api_view(["GET"])
def snippet_list(request):
    try:
        snipets = Sportsman.objects.all()
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = SportSerializer(snipets, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    return Response(status = status.HTTP_404_NOT_FOUND)


@api_view(["GET","POST", "DELETE"])
def snippet(request, pk):
    try:
        snipets = Sportsman.objects.get(pk=pk)
    except:
        return Response(request.error, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer= SportSerializer(snipets) # преобразуем его в питоновски ответ из JSON (сырых данных)
        return Response(serializer.data) # возвращаем ответ

    elif request.method  == "PUT": # тут мы уже сами отправляет ответ.
        serializer = SportSerializer(snipets, data = request.data) # преобразовали в json
        if serializer.is_valid(): # проверка, что наш сериализатор смог преобразовать данные в JSON
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_404_NOT_FOUND)
    elif request.method == "DELETE":
        snipets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class SportAPIView(APIView): # обработка get запросов
#     def get(self, request):
#         s = Sportsman.objects.all()
#         return Response({'posts': SportSerializer(s, many=True).data})


#     def post(self, request):
#         serializer = SportSerializer(data = request.data)
#         serializer.is_valid(raise_exception = True)

#         serializer.save()
#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response("Method put is not defined")

#         try:
#             instance = Sportsman.objects.get(pk = pk)
#         except:
#             return Response("object not found")
        
#         serializer=  SportSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})