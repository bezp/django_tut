from django import forms
from .models import Art



class AsciiForm(forms.ModelForm):

    class Meta:
        model = Art
        fields = ['title', 'art'] #'__all__'
        labels = {
            'title': 'Yo name',
            'art': 'where u think u from'
        }