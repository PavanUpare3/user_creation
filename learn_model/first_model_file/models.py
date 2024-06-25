from django.db import models

class StudentModel(models.Model):
    name= models.CharField(max_length=23)
    password = models.CharField(max_length=34)
    number = models.IntegerField()
    email = models.EmailField()
