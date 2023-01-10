from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.apioverview, name = 'api_view'),
    path('tasks/', views.all_tasks, name = 'all_tasks'),
    path('tasks/<str:pk>/', views.particular_task, name = 'particular_task'),
    path('users/', views.all_users, name = 'all_users'),
    path('user/<str:pk>/', views.user_task, name = 'user_task'),
]