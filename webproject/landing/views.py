import os

from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.


def homeview(request):
    return render(request, 'landing/home.html')


def about(request):
    return render(request, 'landing/about.html')


def blog(request):
    return render(request, 'landing/blog.html')


def horaires(request):
    return render(request, 'landing/modale_schedule.html')


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            form.save()
            send_mail(
                'Message de ' + first_name + last_name,  # subject
                message,  # message
                email,  # from email
                ['you.aouali@gmail.com'],  # to email
            )
            return render(request, 'landing/home.html', context={'form': form, 'success': True})
    return render(request, 'landing/home.html', context={ 'form': form, 'success': False })



def blog(request):
    return render(request, 'landing/blog.html')
