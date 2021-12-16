from django.forms import ModelForm
#from address.forms import AddressField



from .models import Cinema


class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        fields = ['name', 'description', 'address', 'cover',]
  