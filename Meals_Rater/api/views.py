
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . serializer import MealSerializer,RatingSerializer , UserSerializer
from . models import Meal,Rating
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny


class Userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key, }, status=status.HTTP_201_CREATED)
    
    #for dont anyone show list users in db
    def list(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    

    #def delete(self,request,pk,*args,**kargs):
    #    user = User.objects.get(id=pk)
    #    user.delete()
    #    json = {
    #        'message': "the user is deleted",
    #    }
    #    return Response(json, status=status.HTTP_200_OK)        


class Mealviewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    
    @action(detail=True, methods=['post','put'])
    def reat_meal(self, request, pk=None):
        if 'stars' in request.data:
            # update or create

            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            #user = request.data['user']
            #user = User.objects.get(username=username)  # complate element for [id,name,.....]
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

