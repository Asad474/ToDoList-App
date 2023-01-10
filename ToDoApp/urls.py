from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('updatetask/<str:pk>/', views.updatetask, name='updatetask'),
    path('deletetask/<str:pk>/', views.deletetask, name='deletetask'),
    path('login/', views.loginpage, name = 'loginuser'),
    path('logout/', views.logoutpage, name = 'logoutuser'),
    path('register/', views.registeruser, name = 'registeruser'),
    path('userprofile/<str:pk>/', views.userprofile, name = 'userprofile'),
    path('editprofile/', views.updateprofile, name = 'update-profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'ToDoApp/password_reset.html'), name = 'password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='ToDoApp/password_reset_done.html'), name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'ToDoApp/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name = 'ToDoapp/password_reset_complete.html'
         ),
         name = 'password_reset_complete'),
]