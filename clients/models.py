from django.db import models

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=30)
    client_phone = models.CharField(max_length=12)
    client_email = models.EmailField()
    client_work = models.CharField(max_length=30)