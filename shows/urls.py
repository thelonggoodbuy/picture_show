from django.urls import path

from .views import CinemaCreateView


urlpatterns = [
    path('create_cinema/', CinemaCreateView.as_view(), name="create_show")
]