from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


from .models import CustomUser, CustomAdminUser, MainUser


class CustomUserCreationForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = MainUser
        fields = ("email", )
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_simple_user = True
        user.save()
        simple_user = CustomUser.objects.create(user=user)
        return user
        


class CustomAdminCreationForm(UserCreationForm):


    class Meta(UserCreationForm):
        model = CustomAdminUser
        fields = ("email", )
