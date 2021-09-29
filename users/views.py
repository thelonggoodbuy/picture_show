from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth import login


from .forms import CustomUserCreationForm, CustomAdminCreationForm
from .models import CustomUser

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'simple_user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    
class SignUpAdminView(CreateView):
    form_class = CustomAdminCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup_admin.html'