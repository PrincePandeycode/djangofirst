
from django.db import models


# Create your models here.
class Contact(models.Model):   #model is a info about data not table or data itself
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    addr = models.TextField()
    desc = models.TextField()

    def __str__(self):
        return self.name +" - "+ self.email

