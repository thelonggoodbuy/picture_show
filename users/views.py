from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth import login


from .forms import CustomUserCreationForm#, CustomAdminCreationForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
