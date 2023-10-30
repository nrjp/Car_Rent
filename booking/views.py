from django.shortcuts import render
from .forms import BookingForm,ReturnForm
from django.contrib import messages
from .models import BookingModel
from rest_framework import generics
from .serializers import CarSerializer
import logging

logger = logging.getLogger("main")
# Car booking
def booking(request):
	form = BookingForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			messages.success(request, "Car Booking Added...")
	return render(request, 'booking.html', {'form':form})

# show all records
def show_bookings(request, booking_number=None):
    logger.error('hello')
    if booking_number:
        bookings = BookingModel.objects.filter(booking_number=booking_number)
    else:
        bookings = BookingModel.objects.all()

    return render(request, 'show_booking.html', {'bookings': bookings})

# add car return and calculate rent
def car_return(request, booking_number):
    booking = BookingModel.objects.get(booking_number=booking_number)

    if request.method == "POST":
        form = ReturnForm(request.POST, instance=booking)
        if form.is_valid():
            instance = form.save()
            baseDayRental = 90
            total_time = instance.return_datetime - instance.rental_datetime
            numberOfDays = total_time.days
            kilometerPrice = 15
            numberOfKilometers = float(instance.car_mileage_return - instance.car_mileage_request)
            car_cat = str(instance.car_category)
            if car_cat == 'Compact':
                print(instance.car_category)
                rental_price = baseDayRental * numberOfDays
            elif car_cat == 'Premium':
                rental_price = (baseDayRental * numberOfDays * 1.2) + (kilometerPrice * numberOfKilometers)
                print(baseDayRental * numberOfDays * 1.2)
                print(kilometerPrice * numberOfKilometers)
            elif car_cat == 'Minivan':
                rental_price = baseDayRental * numberOfDays * 1.7 + (kilometerPrice * numberOfKilometers * 1.5)
            else:
                rental_price = 0

            instance.rental_price = rental_price
            instance.save()
            context = {'Booking Number':booking.booking_number,'Customer Name':booking.customer_name,'Car Category':booking.car_category,'Rental Price': rental_price,'Number Of Days':numberOfDays,'Number Of Kilometers':numberOfKilometers,'baseDayRental':baseDayRental,'kilometerPrice':kilometerPrice}
            return render(request, 'success.html', {'context': context})    

    else:
        form = ReturnForm(instance=booking)

    return render(request, 'booking.html', {'form': form})       
  
# Rest Api to create car category
class AddCarCategory(generics.CreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = CarSerializer