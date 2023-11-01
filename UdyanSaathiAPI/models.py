# models.py
from django.db import models

class pollutionModel(models.Model):
    State = models.CharField(max_length=255,default=" ")
    City = models.CharField(max_length=255,default=" ")
    Station = models.CharField(max_length=500,default=" ")
    Date = models.DateField(default="2023-10-10")
    CO = models.FloatField(max_length=10,default=0)
    NH3 = models.FloatField(max_length=10,default=0)
    NO2 = models.FloatField(max_length=10,default=0)
    OZONE = models.FloatField(max_length=10,default=0)
    PM25 = models.FloatField(max_length=10,default=0)
    PM10 = models.FloatField(max_length=10,default=0)
    SO2 = models.FloatField(max_length=10,default=0)
    Checks = models.IntegerField(default=0)
    AQI = models.IntegerField(default=0)
    AQI_Quality = models.CharField(max_length=100,default=" ")
