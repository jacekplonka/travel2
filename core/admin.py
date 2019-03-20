from django.contrib import admin
from .models import Trip
from .models import Reservation
from .models import Hotel

# Register your models here.

admin.site.register(Trip)
admin.site.register(Reservation)
admin.site.register(Hotel)
