from rest_framework import serializers
from models.py import Pet
class CustomPetSerializer(serializers.Serializer):
    name=serializers.CharField()
    specie=serializers.CharField()

class PetModelSerializer(serializers.Serializer):
    id=serializers.integerField()
    class Meta:
        model=Pet