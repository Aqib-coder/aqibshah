from django.db import models
from tinymce.models import HTMLField
# from autoslug import AutoSlugField

# Create your models here.
class Service(models.Model):
    service_title = models.CharField(max_length=30)
    service_desc = HTMLField()
    service_slug = str(service_title).replace(" ","-")

