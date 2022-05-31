from django.shortcuts import render
from home.models import Newsletter


def index(request):
    return render(request, 'home/index.html')


def thankyou(request):
    if request.POST:
        newsletter_contact = Newsletter()
        data = request.POST.dict()
        user_signup = data.get('signup')
        newsletter_contact.email = user_signup
        newsletter_contact.save()
    return render(request, 'home/thankyou.html')
