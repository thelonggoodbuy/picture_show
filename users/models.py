from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy


from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(ugettext_lazy('email adress'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    