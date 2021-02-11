from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):


    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', )
        exclude = ['username',]