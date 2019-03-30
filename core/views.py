from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Trip, Reservation, Country
from .forms import SearchForm, ReservationForm
from django.db.models import Q

import datetime


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class IndexView(View):
    def get(self, request, order='departure_date'):
        query = {}
        form = SearchForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['destination'] != '':
                destination = form.cleaned_data['destination'].capitalize()
                date = form.cleaned_data['date']
                trips = Trip.objects.filter(Q(country__name=destination)
                                            | Q(hotel__name__contains=destination)
                                            | Q(name__contains=destination)).order_by(order)
                query = {
                    'destination': destination
                }
                if date is not None:
                    query = {
                        'date': date,
                        'destination': destination
                    }
                    trips = trips.filter(departure_date__gte=date)

            elif form.cleaned_data['date'] is not None:
                trips = Trip.objects.filter(departure_date__gte=form.cleaned_data['date'])
                query = {
                    'date': form.cleaned_data['date']
                }
            else:
                trips = Trip.objects.all().order_by(order)
        else:
            trips = Trip.objects.all().order_by(order)

        return render(request, "index.html", {'trips': trips, 'form': form, 'order': order, 'query': query})


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
            reservations = Reservation.objects.filter(user=request.user)

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
