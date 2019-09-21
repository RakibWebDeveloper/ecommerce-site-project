from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate
)
from .models import User


class UserRegistrationFrom(UserCreationForm):
    # first_name = forms.CharField(max_length=255, label='First Name')
    # last_name = forms.CharField(max_length=255, label='Last Name')
    # hobby = forms.CharField(max_length=255, label='Hobby')
    # avater = forms.ImageField(label='Avater')

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'avater',
            'password1', 'password2'
        ]
        