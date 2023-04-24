from django.contrib import admin
from . models import JobModel, CategoryModel, Candidates

# Register your models here.

admin.site.register(JobModel)
admin.site.register(CategoryModel)
admin.site.register(Candidates)