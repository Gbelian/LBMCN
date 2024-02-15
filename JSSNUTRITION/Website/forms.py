from django import forms
from .models import Contact
from .models import Inscription
from .models import Newsletters

class InfoForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'


class Contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class Newsletters(forms.ModelForm):
    class Meta:
        model = Newsletters
        fields = '__all__'

from .models import Inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'
