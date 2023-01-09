from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserForm(UserCreationForm):
    class Meta:
        fields=['email','password1','password2','name']
        model=get_user_model()