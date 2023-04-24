from django.db import models
from django.utils.text import slugify

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


JOB_TYPE = [
    ('Full time','Full time'),
    ('Part time','Part time')
]

class JobModel(models.Model):
    
    def imageGenerator(instance, fileName):
        imageName , extension = fileName.split(".")
        return f"jobsImages/{instance.id}.{extension}"

    title = models.CharField(max_length=100)
    #location
    jobType = models.CharField(max_length=50, choices=JOB_TYPE)
    description = models.TextField(max_length=1000, null=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to = imageGenerator, null=True)
    slug = models.SlugField(null=True, blank=True)
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super(JobModel,self).save(*args,**kwargs)
    def __str__(self):
        return self.title    



class Candidates(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to="apply/")
    coverLetter = models.TextField(max_length=100)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name