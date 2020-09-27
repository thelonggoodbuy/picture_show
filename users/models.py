from django.db import models
from django.urls import reverse


class User(models.Model):
    login = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.login