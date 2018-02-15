from django import forms
from django.core import validators


class ContactForm(forms.Form):
    name = forms.CharField(required=True,
                           max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Smith'})
                           )
    email = forms.EmailField(required=True,
                             max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'jsmith@example.com'})
                             )
    message = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Lets do business!'})
                              )
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="Leave empty",
        validators=[validators.MaxLengthValidator(0)])

