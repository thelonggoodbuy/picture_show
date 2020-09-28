from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404

from .models import User


class RegistrationView(CreateView):
    model = User
    template_name = 'registration.html'
    fields = ['login', 'email', 'password']


def success_registration(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {'login': user.login}
    return render(request, 'success_registration.html', context)


def home(request):
    return render(request, 'home.html')