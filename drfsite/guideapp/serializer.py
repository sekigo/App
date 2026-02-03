from rest_framework import serializers
from .models import Sportsman
from rest_framework.renderers import JSONRenderer



# class SportsmanModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content



class SportSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 40)
    age = serializers.IntegerField()
    time_created = serializers.DateTimeField(read_only = True)
    time_update = serializers.DateTimeField(read_only = True)
    is_active = serializers.BooleanField(default = True)
    cat_id = serializers.IntegerField()


    def create(self, validated_data):
        return Sportsman.objects.create(**validated_data)


    def update(self, instance,validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        time_update = validated_data.get("time_updated", instance.time_update)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance
        


# def encode():
#     model = SportsmanModel("Ippo", "content: best boxer")
#     model_sr = SportSerializer(model)
#     print(model_sr.data, type(model_sr), sep = '\n')
    
#     json = JSONRenderer().render(model_sr.data)

#     print(json)

