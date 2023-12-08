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
    Date = models.DateField(default="2023-10-10")
class pollutionModel(models.Model):
    State = models.CharField(max_length=255, default=" ")
    City = models.CharField(max_length=255, default=" ")
    Station = models.CharField(max_length=500, default=" ")
    Date = models.DateTimeField(default=datetime(2023, 10, 10, 23, 0, 0))
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

    def clean(self):
        # Ensure that the Date field is a datetime object
        if isinstance(self.Date, str):
            # Convert the string to a datetime object
            try:
                # Try to parse as the original format
                self.Date = datetime.strptime(self.Date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                # If parsing fails, assume it's already in the desired format
                self.Date = datetime.strptime(self.Date, "%Y-%m-%dT%H:%M:%SZ")

        # Set minutes and seconds to zero
        self.Date = self.Date.replace(minute=0, second=0)
    def save(self, *args, **kwargs):
        # Call clean before saving
        self.clean()

        super().save(*args, **kwargs)
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
    Date = models.DateField(default="2023-10-10")
