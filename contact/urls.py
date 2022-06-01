from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', index, name='contact'),
    path('thankyou_contact/', thankyou_contact, name='thankyou_contact'),
]
