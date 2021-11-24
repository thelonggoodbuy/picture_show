from django.urls import path

from .views import CinemaListView, CinemaCreateView, CinemaUpdateView, CinemaDetailView, CinemaDeleteView 


urlpatterns = [
    path('', CinemaListView.as_view(), name="cinema_list"),
    path('<int:pk>/', CinemaDetailView.as_view(), name="cinema_detail"),
    path('cinema_create/', CinemaCreateView.as_view(), name="cinema_create"),
    path('<int:pk>/cinema_edit/', CinemaUpdateView.as_view(), name="cinema_edit"),
    path('<int:pk>/cinema_delete/', CinemaDeleteView.as_view(), name="cinema_delete"),
]