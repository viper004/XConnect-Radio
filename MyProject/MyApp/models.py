from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(unique=True,max_length=150,null=False)
    date_of_birth=models.DateField()
    email=models.EmailField(null=False)
    password=models.CharField(max_length=150,null=False)
    user_type=models.IntegerField(null=False)
    created_time=models.TimeField(auto_now_add=True,null=False)
    created_date=models.DateField(auto_now_add=True,null=False)