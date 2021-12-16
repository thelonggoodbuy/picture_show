from django.urls import path

from .views import CinemaListView, CinemaCreateView, CinemaUpdateView, CinemaDetailView, CinemaDeleteView 


urlpatterns = [
    path('cinema/', CinemaListView.as_view(), name="cinema_list"),
    path('cinema/<int:pk>/', CinemaDetailView.as_view(), name="cinema_detail"),
    path('cinema/cinema_create/', CinemaCreateView.as_view(), name="cinema_create"),
    path('cinema/<int:pk>/cinema_edit/', CinemaUpdateView.as_view(), name="cinema_edit"),
    path('cinema/<int:pk>/cinema_delete/', CinemaDeleteView.as_view(), name="cinema_delete"),
]