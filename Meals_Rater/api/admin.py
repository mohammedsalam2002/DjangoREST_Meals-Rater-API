from django.contrib import admin
from . models import Meal,Rating
# Register your models here
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# for User Admin in Django
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)




class MealAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('id')
    
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'description']
    list_filter = ['title', 'description']


class RatingAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('id')
    
    list_display = ['id', 'meal', 'user', 'stars']
    list_filter = ['meal', 'user']


   
    
admin.site.register(Meal,MealAdmin)
admin.site.register(Rating,RatingAdmin)
