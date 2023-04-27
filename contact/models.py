from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    place = models.CharField(max_length=100, null=True)
    phoneNumber = models.IntegerField(null=True)
    email = models.EmailField(max_length=50,null=True)

    def __str__(self):
        return self.email
