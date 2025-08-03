from django.db import models
from tinymce.models import HTMLField
# from autoslug import AutoSlugField

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=30)
    project_tech = HTMLField()
    project_desc = HTMLField()
    project_image = models.FileField()
    project_slug = models.CharField(max_length=30)