from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.
class Athlete(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def slug(self): #slug for url management in later implementations
        return slugify(self.name)


class Session(models.Model):
    date = models.DateTimeField(default=timezone.now) #

    def __str__(self):
        return str(self.date)


class Jump(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    position_graph = models.ImageField()

    speed_graph = models.ImageField()

    stride_graph = models.ImageField()

    #update to postgres to include json
    #json_file = models.JSONField()