from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField(max_length=40)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    departure_date = models.DateField()
    return_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    short_desc = models.TextField(max_length=512)
    long_desc = models.TextField(max_length=2048)
    photo1 = models.ImageField(upload_to="trips", default="null")
    photo2 = models.ImageField(upload_to="trips", default="null")
    photo3 = models.ImageField(upload_to="trips", default="null")
    photo4 = models.ImageField(upload_to="trips", default="null")
    photo5 = models.ImageField(upload_to="trips", default="null")
    photo6 = models.ImageField(upload_to="trips", default="null")
    photo7 = models.ImageField(upload_to="trips", default="null")
    photo8 = models.ImageField(upload_to="trips", default="null")
    photo9 = models.ImageField(upload_to="trips", default="null")
    photo10 = models.ImageField(upload_to="trips", default="null")

    def __str__(self):
        return self.name


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

