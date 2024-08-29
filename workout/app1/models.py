from django.db import models

# Create your models here.
class Studentinfo(models.Model):
    name=models.CharField(max_length=250)
    classs=models.IntegerField(null=True)
    dep=models.CharField(max_length=250)

