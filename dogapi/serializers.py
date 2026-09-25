from rest_framework import serializers
from .models import Dog, Breed

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Dog
        fields = '__all__'#['name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Breed
        fields = '__all__'#['name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']