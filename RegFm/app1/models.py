from django.db import models

# Create your models here.
class Register(models.Model):
    Fullname =models.CharField(max_length=50)
    Email =models.EmailField()
    Phone =models.CharField(max_length=30)
    Gender =models.CharField(max_length=10,default=" ")
    Desc =models.TextField(blank=True)

    def __str__(self):
        return self.Fullname