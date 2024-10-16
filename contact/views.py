from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            send_mail(
                subject=f"New message from {contact.email}",
                message=contact.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            messages.success(request,
                             'Your message has been sent successfully!')

            return redirect('contact')
    else:
        if request.user.is_authenticated:
            user = request.user
            form = ContactForm(initial={
                'email': user.email,
                'name': user.username,
            })
        else:
            form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
