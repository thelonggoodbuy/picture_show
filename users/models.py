from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass