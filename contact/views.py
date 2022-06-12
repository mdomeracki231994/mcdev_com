from django.shortcuts import render
from utils.common.send_email import mail_send
from contact.models import ContactFormData


def index(request):
    return render(request, 'contact/index.html')


def thankyou_contact(request):
    if request.POST:
        customer_contact = ContactFormData()
        data = request.POST.dict()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')
        customer_contact.name = name
        customer_contact.email = email
        customer_contact.phone_number = phone
        customer_contact.message = message
        mail_send(name, email, phone, message)
        customer_contact.save()
    return render(request, 'contact/thankyou.html')
