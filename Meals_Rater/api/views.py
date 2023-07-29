
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . serializer import MealSerializer,RatingSerializer
from . models import Meal,Rating
from rest_framework.response import Response

class Mealviewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
    
class Ratingviewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

