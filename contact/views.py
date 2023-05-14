from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

# Create your views here.


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)
