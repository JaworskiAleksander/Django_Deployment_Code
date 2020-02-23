from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, DeleteView,
                                UpdateView)
from . import models

# Create your views here.

# this view is what users will see when loading main page
class IndexView(TemplateView):
    template_name = 'index.html'

class CRUD_SystemIndex(TemplateView):
    template_name = 'CRUD_System/index.html'

# this class is responsible for displaying list of all schools
# School views
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'CRUD_ListView.html'

class SchoolCreateView(CreateView):
    context_object_name = 'add_school'
    template_name = 'CRUD_System/CRUD_FormView.html'
    model = models.School
    fields = ('name', 'location')

    def get_success_url(self):
        return reverse('CRUD_System:schools')

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'CRUD_System/CRUD_DetailView.html'

class SchoolUpdateView(UpdateView):
    fields = '__all__'
    model = models.School
    template_name = 'CRUD_System/CRUD_FormView.html'

class SchoolDeleteView(DeleteView):
    model = models.School

    def get_success_url(self):
        return reverse('CRUD_System:schools')
    
# Student views
class StudentListView(ListView):
    context_object_name = 'students'
    model = models.Student
    template_name = 'CRUD_ListView.html'

class StudentCreateView(CreateView):
    context_object_name = 'add_student'
    model = models.Student
    template_name = 'CRUD_System/CRUD_FormView.html'
    fields = ('name', 'last_name', 'school')

    def get_success_url(self):
        return reverse('CRUD_System:students')

class StudentDetailView(DetailView):
    context_object_name = 'student_details'
    model = models.Student
    template_name = 'CRUD_System/CRUD_DetailView.html'

class StudentUpdateView(UpdateView):
    fields = '__all__'
    model = models.Student
    template_name = 'CRUD_System/CRUD_FormView.html'

class StudentDeleteView(DeleteView):
    model = models.Student

    def get_success_url(self):
        return reverse('CRUD_System:students')
    
# Principal views
class PrincipalListView(ListView):
    context_object_name = 'principals'
    model = models.Principal
    template_name = 'CRUD_ListView.html'

class PrincipalCreateView(CreateView):
    context_object_name = 'add_principal'
    template_name = 'CRUD_System/CRUD_FormView.html'
    model = models.Principal
    fields = ('name', 'last_name', 'school')

    def get_success_url(self):
        return reverse('CRUD_System:principals')

class PrincipalDetailView(DetailView):
    context_object_name = 'principal_details'
    model = models.Principal
    template_name = 'CRUD_System/CRUD_DetailView.html'

class PrincipalUpdateView(UpdateView):
    fields = '__all__'
    model = models.Principal
    template_name = 'CRUD_System/CRUD_FormView.html'

class PrincipalDeleteView(DeleteView):
    model = models.Principal

    def get_success_url(self):
        return reverse('CRUD_System:principals')