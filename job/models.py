from django.db import models

# Create your models here.


JOB_TYPE = [
    ('Full time','Full time'),
    ('Part time','Part time')
]

class JobModel(models.Model):

    title = models.CharField(max_length=100)
    #location
    jobType = models.CharField(max_length=50, choices=JOB_TYPE)
    description = models.TextField(max_length=1000, null=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title