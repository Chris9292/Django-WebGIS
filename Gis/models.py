from django.contrib.gis.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    city = models.CharField(max_length=50)
    #img = models.ImageField()

    # returns the string representetion of the model
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(default="testUser", max_length=15)
    location = models.PointField()

    def __str__(self):
        return self.name
