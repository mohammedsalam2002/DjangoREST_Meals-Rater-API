from rest_framework import serializers
from . models import Rating,Meal
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','stars','user','meal')

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id','title','description','avg_of_ratings','num_of_ratings')