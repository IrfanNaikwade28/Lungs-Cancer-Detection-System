# pridiction/admin.py

from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'gender', 'email', 'city', 'pincode','data_image')


admin.site.register(UserProfile, UserProfileAdmin)

