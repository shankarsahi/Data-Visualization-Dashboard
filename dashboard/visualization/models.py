from django.db import models

# Create your models here.
from django.db import models

class DataPoint(models.Model):
    intensity = models.FloatField()
    likelihood = models.FloatField()
    relevance = models.FloatField()
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    topics = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    pest = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    swot = models.CharField(max_length=255)