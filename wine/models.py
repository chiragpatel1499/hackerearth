from django.db import models

# Create your models here.
class WineData(models.Model):
    id = models.AutoField(primary_key = True)
    country = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100000)
    designation = models.CharField(max_length = 10000)
    points = models.IntegerField(max_length = 10)
    price = models.IntegerField(max_length = 10)
    province = models.CharField(max_length = 100)
    region_1 = models.CharField(max_length = 100)
    region_2 = models.CharField(max_length = 100)
    variety = models.CharField(max_length = 100)
    winery = models.CharField(max_length = 100)