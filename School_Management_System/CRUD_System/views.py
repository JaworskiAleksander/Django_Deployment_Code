from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, DeleteView,
                                UpdateView)
from . import models

# Create your views here.

# this view is what users will see when loading main page
class IndexView(TemplateView):
    template_name = 'index.html'

# this class is responsible for displaying list of all schools
class SchoolListView(ListView):
    context_object_name = 'school_list'
    model = models.School
    # template_name = 'CRUD_System/CRUD_System_schools.html'


class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
