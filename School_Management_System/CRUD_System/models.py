from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 256)
    location = models.CharField(max_length = 256)
    
class Principal(models.Model):
    name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # picture = models.ImageField()

class Student(models.Model):
    name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')