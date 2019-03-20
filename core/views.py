from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .models import Trip, Reservation


# Create your views here.


class IndexView(View):
    def get(self, request):
        trips = Trip.objects.all()
        for trip in trips:
            trip.photos = []
            trip.photos.append(trip.photo1.url)
            trip.photos.append(trip.photo2.url)
            trip.photos.append(trip.photo3.url)
            trip.photos.append(trip.photo4.url)
            trip.photos.append(trip.photo5.url)
            trip.photos.append(trip.photo6.url)
            trip.photos.append(trip.photo7.url)
            trip.photos.append(trip.photo8.url)
            trip.photos.append(trip.photo9.url)
            trip.photos.append(trip.photo10.url)
        return render(request, "index.html", {'trips': trips})


class TripView(View):
    def get(self, request, id):
        trip = get_object_or_404(Trip, id=id)
        return render(request, "trip.html", {'trip': trip})


class ReservationView(View):
    def get(self, request):
        if request.user.is_authenticated:
            reservations = Reservation.objects.all().filter(user=request.user.id)

            return render(request, 'reservations.html', {'reservations': reservations})
        return redirect('/accounts/login/')
