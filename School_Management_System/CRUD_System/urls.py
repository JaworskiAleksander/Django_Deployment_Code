from django.urls import path, include
from . import views

app_name = 'CRUD_System'

urlpatterns = [    
    path('', views.CRUD_SystemIndex.as_view(), name='CRUD_Index'),
    path('schools/', views.SchoolListView.as_view(), name='schools'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('principals/', views.PrincipalListView.as_view(), name='principals'),

    path('add_school/', views.SchoolCreateView.as_view(), name='add_school'),
    path('add_student/', views.StudentCreateView.as_view(), name='add_student'),
    path('add_principal/', views.PrincipalCreateView.as_view(), name='add_principal'),

    path('principals/<int:pk>', views.PrincipalDetailView.as_view(), name='principal_details'),
    path('schools/<int:pk>', views.SchoolDetailView.as_view(), name='school_details'),
    path('students/<int:pk>', views.StudentDetailView.as_view(), name='student_details'),

    path('principals/update/<int:pk>', views.PrincipalUpdateView.as_view(), name='principal_update'),
    path('schools/update/<int:pk>', views.SchoolUpdateView.as_view(), name='school_update'),
    path('students/update/<int:pk>', views.StudentUpdateView.as_view(), name='student_update'),
    
    path('principals/delete/<int:pk>', views.PrincipalDeleteView.as_view(), name='principal_delete'),
    path('schools/delete/<int:pk>', views.SchoolDeleteView.as_view(), name='school_delete'),
    path('students/delete/<int:pk>', views.StudentDeleteView.as_view(), name='student_delete'),
]
