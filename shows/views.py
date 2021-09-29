from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Cinema
from .forms import AddCinemaForm


class CinemaListView(ListView):
    model = Cinema
    template_name = "cinema_list.html"


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



class CinemaUpdateView(UpdateView):
    model = Cinema
    template_name = "cinema_edit.html"
    fields = ('name', 'description', 'address', 'cover',)


class CinemaDetailView(DetailView):
    model = Cinema
    template_name = "cinema_detail.html"


class CinemaDeleteView(DeleteView):
    model = Cinema
    template_name = "cinema_delete.html"
    success_url = reverse_lazy('cinema_list')
