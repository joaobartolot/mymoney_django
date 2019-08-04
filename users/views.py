from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import ProfileCreationForm

# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = ProfileCreationForm
    success_url = '/login/'

    template_name = 'users/user_form.html'