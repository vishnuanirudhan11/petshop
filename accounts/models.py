from django.db import models

# Create your models here.


class user(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    username=models.CharField(max_length=250,unique=True)
    password=models.CharField(max_length=250)
    birthday=models.DateTimeField()
    gender=models.BooleanField(default=True)
    email=models.CharField(max_length=250,unique=True)
    phone=models.IntegerField()
