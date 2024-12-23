from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path("register/", views.UserCreateView.as_view(), name="register")
]