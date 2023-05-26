from django.db import models
from tinymce.models import HTMLField

# Create your models here.
#class post(models.Model):
 #   title=models.CharField(max_length=100)
  ## image=models.FileField(upload_to="news/",max_length=250,null=True,default=None)
   # post_image=AutoSlugField(populate_from='post_title',unique=True,null=True,default=None)
#    def _str_(self):
 #       return self.title
class Files(models.Model):
    file_title=models.CharField(max_length=100)
    file_desc=HTMLField()
    file_pdf=models.FileField(upload_to="news/",max_length=250,null=True,default=None)