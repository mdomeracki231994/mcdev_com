from django.db import models


class Newsletter(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
