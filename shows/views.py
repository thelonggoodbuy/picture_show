from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Cinema
from users.models import CustomUser
from .forms import CinemaForm



class SuperUserTestMixin(LoginRequiredMixin, UserPassesTestMixin):
    model = CustomUser


    def test_func(self):
        if self.request.user.is_superuser:
            return self.request.user.is_superuser == True

        


class CinemaListView(SuperUserTestMixin, ListView):
    model = Cinema
    template_name = "cinema_list.html"
    context_object_name = 'cinemas'


class CinemaCreateView(SuperUserTestMixin, CreateView):
    model = Cinema
    template_name = "cinema_new.html"
    form_class = CinemaForm
    success_url = reverse_lazy('cinema_list')

    def upload_image_cover(request):
        if request.method == 'POST':
            form = CinemaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/shows/')
        else:
            form = CinemaForm()
        return render(request, 'cinema_new.html', {'form': form})


class CinemaUpdateView(SuperUserTestMixin, UpdateView):
    model = Cinema
    template_name = "cinema_edit.html"
    fields = ('name', 'description', 'address', 'cover',)


class CinemaDetailView(SuperUserTestMixin, DetailView):
    model = Cinema
    template_name = "cinema_detail.html"


class CinemaDeleteView(SuperUserTestMixin, DeleteView):
    model = Cinema
    template_name = "cinema_delete.html"
    success_url = reverse_lazy('cinema_list')
