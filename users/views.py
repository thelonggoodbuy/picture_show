from django.shortcuts import render, redirect
#from django.views import View
from django.http import HttpResponseRedirect


from .forms import RegistrationForm


#class RegistrationFormView(View):
#    form_class = RegistrationForm
#    templatename = 'registration'
#
#    def post(self, request):
#        form = self.form_class(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect('/registration_success/')

#        return render(request, self.template_name, {'form': form})


def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        user = form.save(commit=False)
        return redirect('success_registration_view', pk=user.pk)

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})



def success_registration_view(request):
    return render(request, 'success_registration.html', {})
