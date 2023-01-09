from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
from .models import Task

class CustomUserForm(UserCreationForm):
    class Meta:
        fields=['email','password1','password2','name']
        model=get_user_model()


class TaskForm(ModelForm):
    class Meta:
        fields=['title','description']
        model=Task
