from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm




def send_email(request):
    contacts = Contact.objects.all()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank you for contacting us.. We will get back to you soon!')    
            return redirect(reverse('contact'))
    else:
        contact_form = ContactForm()

    context = {
        'contacts': contacts,
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
