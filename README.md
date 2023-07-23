# Car Rental Service


## Web application that allows users to book cars and manage car bookings.

### Features

<ol>
  <li>Users can create new car bookings by providing details such as booking number, customer name, car category, rental datetime, and car mileage at pick-up</li>
  <li>The application calculates the rental price based on the car category, rental duration, and car mileage at pick-up and return</li>
  <li>Users can update the return details for a car booking, including the return datetime and car mileage at return</li>
</ol>

## Install
```
https://github.com/nrjp/Car_Rent
```

```
pip install -r requirements.txt
```
## Run

```
python manage.py runserver
```


### API

#### Car Booking - http://localhost:8000/car_booking/
#### Car Return  - http://localhost:8000/car_return/<booking number>
#### Add car category - http://localhost:8000/add_category/
