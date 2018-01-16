from django import forms
from .models import Art


class AsciiForm(forms.ModelForm):

    class Meta:
        model = Art
        fields = ['title', 'art'] #'__all__'
        labels = {
            'title': 'Alias from da wae',
            'art': 'Message for da wae',
        }
        help_texts = {
            'title': ('(Username)'),
            'art': ('Message you want to send to the masses'),
        }