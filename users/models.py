from django.db import models

class Email(models.Model):
    email = models.TextField(max_length=100)
