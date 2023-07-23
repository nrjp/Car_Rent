from django import forms
from .models import BookingModel

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ['booking_number', 'customer_name', 'car_category', 'rental_datetime', 'car_mileage_request']

class ReturnForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ['booking_number', 'return_datetime', 'car_mileage_return']