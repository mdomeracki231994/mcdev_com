from django.urls import path
from . views import *

urlpatterns = [
    path('services/', index, name="services")
]
