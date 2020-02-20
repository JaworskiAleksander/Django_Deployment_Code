from django.contrib import admin
from CRUD_System.models import School, Student, Principal

# Register your models here.
admin.site.register(School)
admin.site.register(Principal)
admin.site.register(Student)