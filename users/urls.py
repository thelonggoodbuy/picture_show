from django.urls import path

from .views import SignUpView, SignUpAdminView


urlpatterns = [

    path('signup/', SignUpView.as_view(), name="signup"),
    path('signup_admin/', SignUpAdminView.as_view(), name="signup_admin"),

]