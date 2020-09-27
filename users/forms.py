from django.forms import ModelForm


from .models import User


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('login', 'email', 'password',)