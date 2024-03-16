# pridiction/models.py

from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    data_image=models.FileField(upload_to="",max_length=250,null=True,default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
