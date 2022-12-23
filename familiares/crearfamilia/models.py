from django.db import models

# Create your models here.

class Familiar(models.Model):
    name = models.CharField(max_length= 30)
    surname = models.CharField(max_length= 30)
    age = models.IntegerField()
    birthday = models.DateField()