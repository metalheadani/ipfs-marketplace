from django.contrib import admin

from .models import FileUpload, IpfsAddress

admin.site.register(FileUpload)
admin.site.register(IpfsAddress)