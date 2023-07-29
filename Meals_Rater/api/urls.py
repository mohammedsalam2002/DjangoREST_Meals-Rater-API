from django.urls import path
from . views import Mealviewset,Ratingviewset
from django.conf.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('meals', Mealviewset)
router.register('ratings', Ratingviewset)

urlpatterns = [
    path('',include(router.urls)),

]