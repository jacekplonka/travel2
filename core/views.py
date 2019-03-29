from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .models import Trip, Reservation
from .forms import SearchForm, ReservationForm
import datetime
import random


# Create your views here.


class IndexView(View):
    def get(self, request, order='departure_date'):
        trips = Trip.objects.all().order_by(order)

        # for trip in trips:
        #     trip.photos = []
        #     trip.photos.append(trip.photo1.url)
        #     trip.photos.append(trip.photo2.url)
        #     trip.photos.append(trip.photo3.url)
        #     trip.photos.append(trip.photo4.url)
        #     trip.photos.append(trip.photo5.url)
        #     trip.photos.append(trip.photo6.url)
        #     trip.photos.append(trip.photo7.url)
        #     trip.photos.append(trip.photo8.url)
        #     trip.photos.append(trip.photo9.url)
        #     trip.photos.append(trip.photo10.url)
        form = SearchForm()
        return render(request, "index.html", {'trips': trips, 'form': form, 'order': order})


class TripView(View):
    def get(self, request, id):
        trip = get_object_or_404(Trip, id=id)

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
        return render(request, "trip.html", {'trip': trip})


class ReservationView(View):
    def get(self, request):
        if request.user.is_authenticated:
            reservations = Reservation.objects.all().filter(user=request.user)

            return render(request, 'reservations.html', {'reservations': reservations})
        return redirect('/accounts/login/')


class NewReservationView(View):
    def get(self, request, id):
        form = ReservationForm()
        trip = get_object_or_404(Trip, id=id)
        return render(request, 'newReservation.html', {'trip': trip, 'form': form})

    def post(self, request, id):
        trip = get_object_or_404(Trip, id=id)

        form = ReservationForm(request.POST)

        if form.is_valid() and trip.free_rooms >= form.cleaned_data['rooms'] and form.cleaned_data['rooms'] > 0:
            reservation = Reservation()
            reservation.user = request.user
            reservation.trip = trip
            reservation.rooms = form.cleaned_data['rooms']
            reservation.time = datetime.datetime.now()
            reservation.save()
            trip.free_rooms -= form.cleaned_data['rooms']
            trip.save()
            return redirect('/reservations/')
        else:
            form = ReservationForm()
            trip = get_object_or_404(Trip, id=id)
            return render(request, 'newReservation.html', {'trip': trip, 'form': form, 'error': 'Not enough free rooms'})


# class Script(View):
#     def get(self, request):
#         trips = Trip.objects.all()
#         for trip in trips:
#             trip.free_rooms = random.randrange(1,12)
#             trip.save()

