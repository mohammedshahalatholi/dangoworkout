from django.db import models

# Create your models here.
class Admissioninfo(models.Model):
    regno=models.CharField(max_length=30)
    regdate=models.IntegerField(null=True)
    name=models.CharField(max_length=30)
