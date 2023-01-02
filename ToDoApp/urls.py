from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('updatetask/<str:pk>/', views.updatetask, name='updatetask'),
    path('deletetask/<str:pk>/', views.deletetask, name='deletetask'),
]