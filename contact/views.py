from django.shortcuts import render

from contact.models import ContactFormData


def index(request):
    return render(request, 'contact/index.html')


def thank_you(request):
    if request.POST:
        customer_contact = ContactFormData
        data = request.POST.dict()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')
        customer_contact.name = name
        customer_contact.email = email
        customer_contact.phone_number = phone
        customer_contact.message = message
        customer_contact.save()
    return render(request, 'contact/thankyou.html')
