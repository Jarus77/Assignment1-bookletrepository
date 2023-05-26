from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Files(models.Model):
    file_title=models.CharField(max_length=100)
    file_desc=HTMLField()