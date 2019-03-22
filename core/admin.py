from django.contrib import admin
from .models import Trip
from .models import Reservation
from .models import Hotel
from image_cropping import ImageCroppingMixin


# Register your models here.


class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Trip, MyModelAdmin)
admin.site.register(Reservation)
admin.site.register(Hotel)
