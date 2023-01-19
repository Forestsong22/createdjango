from django.db import models

# Create your models here.
class human(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField(default=1)

class color(models.Model):
  red = models.IntegerField(default=0)
  green = models.IntegerField(default=0)
  blue = models.IntegerField(default=0)


# class color00(models.Model):
#   red0 = models.ManyToManyField(color)
#   green0 = models.ManyToManyField(color)
#   blue0 = models.ManyToManyField(color)
