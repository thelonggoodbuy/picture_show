from django.db import models
from django_google_maps import fields as map_fields
from django.urls import reverse

from address.models import AddressField



class Cinema(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    address = AddressField(blank='True', null='True')
    cover = models.ImageField(upload_to='covers/', blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
    