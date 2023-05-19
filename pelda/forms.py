from django import forms
from .models import Termek 

class TermekForm(forms.ModelForm):
    class Meta:
        model = Termek
        fields = '__all__'

        widgets = {
            'azonosito': forms.TextInput(attrs={'class': 'form-control'}),
            'nev': forms.TextInput(attrs={'class': 'form-control'}),
            'leiras': forms.Textarea(attrs={'class': 'form-control'}),
            'ar': forms.NumberInput(attrs={'class': 'form-control'}),
            'raktaron': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            "azonosito": "Azonosító:",
            "nev": "Név:",
            "leiras": "Leírás:",
            "ar": "Ár:",
            "raktaron": "Raktáron:"
        }
        