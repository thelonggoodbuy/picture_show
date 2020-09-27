from django.urls import path

from . import views


urlpatterns = [

    path('users/registration/', views.registration_view, name='registration'),
    path('users/registration/success_registration/', views.success_registration_view, name='success_registration'),

]