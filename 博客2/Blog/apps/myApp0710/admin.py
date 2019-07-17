from django.contrib import admin
from myApp0710 import models

# Register your models here.

admin.site.register(models.Type)
admin.site.register(models.Author)
admin.site.register(models.Artical)