from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 256)
    location = models.CharField(max_length = 256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CRUD_System:school_details", kwargs={"pk": self.pk})
    

class Principal(models.Model):
    name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # picture = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CRUD_System:principal_details", kwargs={"pk": self.pk})
    

class Student(models.Model):
    name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("CRUD_System:student_details", kwargs={"pk": self.pk})
    