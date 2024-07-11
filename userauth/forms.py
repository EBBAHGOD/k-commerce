from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class User_registration_form(UserCreationForm):
    class Meta:
        model=User
        fields=['email','username','password']
