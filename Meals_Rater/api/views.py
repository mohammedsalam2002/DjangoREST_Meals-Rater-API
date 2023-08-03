
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . serializer import MealSerializer,RatingSerializer
from . models import Meal,Rating
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import status

class Mealviewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


    @action(detail=True, methods=['post'])
    def reat_mael(self, request, pk=None):
        if 'stars' in request.data:
            # update or create

            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['user']
            user = User.objects.get(username=username)  # complate element for [id,name,.....]
            try:
                # Update
                rating = Rating.objects.get(user=user.id ,meal=meal.id) # spesifc elemenr
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    "message": f"The rate of the meal is updated",
                    "rate":serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)
            except Rating.DoesNotExist:
                # create 
                new_ratting = Rating.objects.create(user=user,meal=meal,stars=stars)
                serializer = RatingSerializer(new_ratting,many=False)
                json ={
                    "message":"New Rate Added to this meal ",
                    "rate":serializer.data
                }
                return Response(json,status=status.HTTP_201_CREATED)
        else:
           json = {
               'mesages':'the data not valied'
           }
           return Response(json,status=status.HTTP_400_BAD_REQUEST)

  
class Ratingviewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

