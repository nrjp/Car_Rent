from django.db import models
from datetime import datetime

    
class CarCategory(models.Model):
     category = models.CharField(unique=True, max_length=100)

     def __str__(self):
        return self.category
                                  

class BookingModel(models.Model):
    booking_number = models.IntegerField(primary_key=True,max_length=100,unique=True)
    customer_name = models.CharField(max_length=100,unique=True)
    car_category = models.ForeignKey(CarCategory,on_delete=models.CASCADE)
    rental_datetime = models.DateTimeField(default=datetime.now())
    car_mileage_request = models.DecimalField(max_digits=10, decimal_places=2)
    return_datetime = models.DateTimeField(default=datetime.now())
    car_mileage_return = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def __str__(self):
            return f"Booking: {self.booking_number} - {self.customer_name}"