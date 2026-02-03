from rest_framework import serializers
from .models import Sportsman
from rest_framework.renderers import JSONRenderer



# class SportsmanModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content



class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sportsman
        fields = "__all__"
        



# def encode():
#     model = SportsmanModel("Ippo", "content: best boxer")
#     model_sr = SportSerializer(model)
#     print(model_sr.data, type(model_sr), sep = '\n')
    
#     json = JSONRenderer().render(model_sr.data)

#     print(json)

