from django.db import models


class ContactFormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    message = models.TextField()
