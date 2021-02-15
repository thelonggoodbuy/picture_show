from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(ugettext_lazy('email adress'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    