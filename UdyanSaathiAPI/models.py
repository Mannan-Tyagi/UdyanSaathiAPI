# models.py
from django.db import models
from datetime import datetime
from datetime import date
import re

class graphDataModel(models.Model):
    City = models.CharField(max_length=255,default=" ")
    AQI = models.IntegerField(default=0)
    PM25 = models.FloatField(max_length=10,default=0)
    PM10 = models.FloatField(max_length=10,default=0)
    CO = models.FloatField(max_length=10,default=0)
    OZONE = models.FloatField(max_length=10,default=0)
    SO2 = models.FloatField(max_length=10,default=0)
    NO2 = models.FloatField(max_length=10,default=0)
    NH3 = models.FloatField(max_length=10,default=0)   
    Pol_Date = models.CharField(max_length=500, default=" ")
class pollutionModel(models.Model):
    State = models.CharField(max_length=255, default=" ")
    City = models.CharField(max_length=255, default=" ")
    Station = models.CharField(max_length=500, default=" ")
    Pol_Date = models.CharField(max_length=500, default=" ")
    CO = models.FloatField(max_length=10, default=0)
    NH3 = models.FloatField(max_length=10, default=0)
    NO2 = models.FloatField(max_length=10, default=0)
    OZONE = models.FloatField(max_length=10, default=0)
    PM25 = models.FloatField(max_length=10, default=0)
    PM10 = models.FloatField(max_length=10, default=0)
    SO2 = models.FloatField(max_length=10, default=0)
    Checks = models.IntegerField(default=0)
    AQI = models.IntegerField(default=0)
    AQI_Quality = models.CharField(max_length=100, default=" ")

class stationModel(models.Model):
    Station = models.CharField(max_length=500,default=" ")

class Top10CitiesModel(models.Model):
    City = models.CharField(max_length=255,default=" ")
    AQI = models.IntegerField(default=0)
    PM25 = models.FloatField(max_length=10,default=0)
    PM10 = models.FloatField(max_length=10,default=0)
    CO = models.FloatField(max_length=10,default=0)
    OZONE = models.FloatField(max_length=10,default=0)
    SO2 = models.FloatField(max_length=10,default=0)
    NO2 = models.FloatField(max_length=10,default=0)
    NH3 = models.FloatField(max_length=10,default=0)

class Top10LeastCitiesModel(models.Model):
    City = models.CharField(max_length=255,default=" ")
    AQI = models.IntegerField(default=0)
    PM25 = models.FloatField(max_length=10,default=0)
    PM10 = models.FloatField(max_length=10,default=0)
    CO = models.FloatField(max_length=10,default=0)
    OZONE = models.FloatField(max_length=10,default=0)
    SO2 = models.FloatField(max_length=10,default=0)
    NO2 = models.FloatField(max_length=10,default=0)
    NH3 = models.FloatField(max_length=10,default=0)
class TopMetroCitiesModel(models.Model):
    City = models.CharField(max_length=255,default=" ")
    AQI = models.IntegerField(default=0)
    PM25 = models.FloatField(max_length=10,default=0)
    PM10 = models.FloatField(max_length=10,default=0)
    CO = models.FloatField(max_length=10,default=0)
    OZONE = models.FloatField(max_length=10,default=0)
    SO2 = models.FloatField(max_length=10,default=0)
    NO2 = models.FloatField(max_length=10,default=0)
    NH3 = models.FloatField(max_length=10,default=0)   
class AqiCalendarModel(models.Model):
    City = models.CharField(max_length=255,default=" ")
    AQI = models.IntegerField(default=0)
    Pol_Date = models.CharField(max_length=500, default=" ")

