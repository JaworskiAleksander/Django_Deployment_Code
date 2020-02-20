from django.urls import path, include
from . import views

app_name = 'CRUD_System'

urlpatterns = [    
    path('', views.IndexView.as_view(), name='index'),
    path('school_list/', views.SchoolListView.as_view(), name='school_list')
]
