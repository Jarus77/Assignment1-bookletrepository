from django.contrib import admin
from . import models
from django.contrib.admin.sites import site
# Register your models here.

#class BlogAdminArea(admin.AdminSite):
 #   site_header='Blog Admin Area'

#blog_site=BlogAdminArea(name='BlogAdmin')

#blog_site.register(models.post)

class FilesAdmin(admin.ModelAdmin):
    list_display=('file_title','file_desc')

admin.site.register(models.Files,FilesAdmin) 