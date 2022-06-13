from django.db import models


class Customers(models.Model):
    customer_number = models.AutoField(primary_key=True, null=False)
    customer_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    web_site = models.URLField(max_length=250)
    contact_date = models.DateField()
    additional_information_needed = models.BooleanField(default=False)
    add_date_time = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50)


class CustomerContacts(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    add_date_time = models.DateTimeField()
    user_name = models.CharField(max_length=50)
    customer_number = models.ForeignKey(Customers, on_delete=models.CASCADE)


class CustomerNotes(models.Model):
    notes = models.TextField()
    customer_number = models.ForeignKey(Customers, on_delete=models.CASCADE)
