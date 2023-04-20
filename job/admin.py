from django.contrib import admin
from . models import JobModel,CategoryModel

# Register your models here.

admin.site.register(JobModel)
admin.site.register(CategoryModel)