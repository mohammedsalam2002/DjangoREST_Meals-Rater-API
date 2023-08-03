from audioop import avg
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg, Sum

class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)


    def num_of_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)
    
    def avg_of_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(meal=self)
        #print(f'-----------------------------> {ratings}')
        for count in ratings:
            sum += count.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0
       
    
    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    # def __str__(self):
    #     return self.meal


    class Meta:
        # يعني المستخدم ما يكدر يسسوي meal لأكثر من يوزر
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)
