from django.urls import path, include
from . import views

app_name = 'CRUD_System'

urlpatterns = [    
    path('', views.CRUD_SystemIndex.as_view(), name='CRUD_Index'),
    path('school_list/', views.SchoolListView.as_view(), name='school_list'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('principals/', views.PrincipalListView.as_view(), name='principals')
]
