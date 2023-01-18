from django.db import models

# Create your models here.
class human(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField(default=1)