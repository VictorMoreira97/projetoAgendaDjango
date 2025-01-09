from django.shortcuts import render
from contact.models import Contact


def contact(request, contact_id):
    single_contact = Contact.objects.get(pk=contact_id)

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )