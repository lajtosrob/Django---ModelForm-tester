from django import forms
from .models import Termek 

class TermekForm(forms.ModelForm):
    class Meta:
        model = Termek
        fields = '__all__'
        