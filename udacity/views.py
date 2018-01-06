from django.shortcuts import render
from .models import Art
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
# Create your views here.




def ascii(request):
    xtry = Art.objects.all()
    form = forms.AsciiForm()
    if request.method == 'POST':
        form = forms.AsciiForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('udacity:ascii'))

    return render(request, 'mysite/ascii.html', {'form': form, 'xtry': xtry})



