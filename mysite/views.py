from django.shortcuts import render
from . import forms
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.loader import get_template

def hello_world(request):
    return render(request, 'main_page.html')

def shello_world(request):
    return render(request, 'xtest.html')


def port_prev(request):
    if request.method == 'GET':
        form = forms.ContactForm()
        return render(request, 'port_homepage.html', {'form': form})

    elif request.method == 'POST':
        form = forms.ContactForm(request.POST)

        if form.is_valid():

            # Get values of each field
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            contact_message = form.cleaned_data['message']

            # Get the template and pass the context values
            template =  get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_message': contact_message,
            }
            # Get the entire text content with context
            content = template.render(context)

            # Email address that we defined in settings.py
            from_email = settings.DEFAULT_FROM_EMAIL

            # Sending the email
            send_mail(
                'New message from Contact form', # Subject
                content, # Body
                'Contact <{}>'.format(from_email), # From
                ['abc@example.com'] # To
            )

            # Add a message to inform the user
            messages.add_message(request, messages.SUCCESS, 'Your submission has been received!')

            # Redirect to the same page
            return HttpResponseRedirect(reverse('profilecontact'))

    # return render(request, 'port_homepage.html')