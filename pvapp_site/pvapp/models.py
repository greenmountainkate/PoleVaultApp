from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Athlete(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def slug(self): #slug for url management in later implementations
        return slugify(self.name)