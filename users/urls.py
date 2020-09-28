from django.urls import path

from .views import RegistrationView, success_registration

from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('success_registration/<int:pk>', views.success_registration, name='success_registration')
    
]