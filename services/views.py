from django.shortcuts import render

from services.models import ServicesOffered


def index(request):
    context = ServicesOffered.objects.all()
    return render(request, 'services/index.html', {'context': context})
