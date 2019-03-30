from django.db import models
from django.contrib.auth import get_user_model
from image_cropping import ImageRatioField
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
    price = models.IntegerField()
    free_rooms = models.IntegerField()
    photo1 = models.ImageField(upload_to="trips", default="null")
    photo2 = models.ImageField(upload_to="trips", default="null", blank=True, null=True)
    photo3 = models.ImageField(upload_to="trips", default="null", blank=True, null=True)
    photo4 = models.ImageField(upload_to="trips", default="null", blank=True, null=True)
    photo5 = models.ImageField(upload_to="trips", default="null", blank=True, null=True)
    photo6 = models.ImageField(upload_to="trips", default="null", blank=True, null=True)
    photo7 = models.ImageField(upload_to="trips", default="null", blank=True, null=True)
    photo8 = models.ImageField(upload_to="trips", default="null", blank=True, null=True)
    photo9 = models.ImageField(upload_to="trips", default="null", blank=True, null=True)
    photo10 = models.ImageField(upload_to="trips", default="null", blank=True, null=True)
    cropping = ImageRatioField('photo1', '420x260')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('departure_date',)


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_created=True)
    rooms = models.IntegerField()

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return str(self.user.username) + " " + str(self.trip.name) + " id{" + str(self.id) + "}"

