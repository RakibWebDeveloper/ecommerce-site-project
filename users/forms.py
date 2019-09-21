from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate
)
from .models import User


class UserRegistrationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'avater',
            'password1', 'password2'
        ]
        