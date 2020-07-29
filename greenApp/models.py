from django.db import models

# Create your models here.
class esp(models.Model):
    esp=models.CharField(max_length=10)
    status=models.BooleanField(default=0)

class data(models.Model):
    datetime=models.DateTimeField(auto_now=True)
    soilmoisture1=models.FloatField(default=0)
    soilmoisture2=models.FloatField(default=0)
    soilmoisture3=models.FloatField(default=0)
    soilmoisture4=models.FloatField(default=0)
    soilmoisture5=models.FloatField(default=0)
    soilmoisture6=models.FloatField(default=0)
    soilmoisture7=models.FloatField(default=0)
    soilmoisture8=models.FloatField(default=0)
    p03 = models.FloatField(default=0)
    p05 = models.FloatField(default=0)
    p10 = models.FloatField(default=0)
    p25 = models.FloatField(default=0)
    pm10= models.FloatField(default=0)
    pm25 = models.FloatField(default=0)
    pm100 = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    temperatureEsp = models.FloatField(default=0)
    soiltempC = models.FloatField(default=0)
    soiltempF = models.FloatField(default=0)


  

    