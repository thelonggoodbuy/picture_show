from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Cinema
from .forms import AddCinemaForm

class CinemaCreateView(CreateView):
    model = Cinema
    template_name = "cinema_new.html"
    fields = ['name', 'description', 'address', 'cover',]

    def upload_image_cover(request):
        if request.method == 'POST':
            form = AddCinemaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = AddCinemaForm()
        return render(request, 'cinema_new.html', {'form': form})


