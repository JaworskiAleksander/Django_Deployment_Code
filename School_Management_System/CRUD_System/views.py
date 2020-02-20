from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

# this view is what users will see when loading main page
class IndexView(TemplateView):
    template_name = 'index.html'