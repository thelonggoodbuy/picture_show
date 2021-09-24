from django import forms
from address.forms import AddressField



from .models import Cinema


class AddCinemaForm(forms.Form):
    class Meta:
        model = Cinema
        address = AddressField()
        cover = forms.ImageField()
        fields ="__all__"