from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send an email
            send_mail(
                subject=f"New message from {contact.email}",
                message=contact.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            return redirect('success') 
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def success(request):
    return render(request, 'contact/success.html')
