from django import forms
from .models import Art



class AsciiForm(forms.ModelForm):

    class Meta:
        model = Art
        fields = '__all__'
