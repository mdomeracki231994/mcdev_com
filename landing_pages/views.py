from django.shortcuts import render


def construction(request):
    return render(request, 'landing_pages/construction/construction.html')


def restaurant(request):
    return render(request, 'landing_pages/restaurant/restaurant.html')


def mechanics(request):
    return render(request, 'landing_pages/mechanics/mechanics.html')
