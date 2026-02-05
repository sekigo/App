from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Sportsman
from .serializer import SportSerializer
from rest_framework.decorators  import api_view
from rest_framework.views import APIView


class SnippetList(APIView):


    def get(self, request):
        snipets = Sportsman.objects.all()
        serializer = SportSerializer(snipets, many = True)
        return Response(serializer.data, status =  status.HTTP_200_OK)

    def post(self, request):
        serializer = SportSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Sportsman.objects.get(pk=pk)
        except Sportsman.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SportSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SportSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)















# class SportAPIList(generics.ListCreateAPIView): # реализует get и post
#     queryset = Sportsman.objects.all()
#     serializer_class = SportSerializer
    
# @api_view(["GET"])
# def snippet_list(request):
#     try:
#         snipets = Sportsman.objects.all()
#     except:
#         return Response(status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = SportSerializer(snipets, many = True)
#         return Response(serializer.data, status = status.HTTP_200_OK)
#     return Response(status = status.HTTP_404_NOT_FOUND)


# @api_view(["GET","POST", "DELETE"])
# def snippet(request, pk):
#     try:
#         snipets = Sportsman.objects.get(pk=pk)
#     except:
#         return Response(request.error, status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer= SportSerializer(snipets) # преобразуем его в питоновски ответ из JSON (сырых данных)
#         return Response(serializer.data) # возвращаем ответ

#     elif request.method  == "PUT": # тут мы уже сами отправляет ответ.
#         serializer = SportSerializer(snipets, data = request.data) # преобразовали в json
#         if serializer.is_valid(): # проверка, что наш сериализатор смог преобразовать данные в JSON
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.error, status = status.HTTP_404_NOT_FOUND)
#     elif request.method == "DELETE":
#         snipets.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






