from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", )
            