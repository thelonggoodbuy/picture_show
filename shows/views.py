from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Cinema
from .forms import AddCinemaForm

class CinemaCreateView(CreateView):
    model = Cinema
    template_name = "cinema_new.html"
    fields = ['name', 'description', 'address', 'cover',]

    # def upload_image_cover(request):
    #     pass
