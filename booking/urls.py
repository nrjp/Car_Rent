from django.urls import path
from . import views
import logging

logger = logging.getLogger("main")

urlpatterns = [
    path('', views.show_bookings, name='show_bookings'),
    path('car_booking/',views.booking,name='booking'),
    path('show_bookings/<str:booking_number>/', views.show_bookings, name='show_bookings_number'),
    path('car_return/<str:booking_number>/', views.car_return, name='car_return'),
    path('add_category/', views.AddCarCategory.as_view(), name='create_booking'),
    path('trigger/', views.trigger_signal, name='trigger_signal'),
    path('summarize/', views.summarize_view, name='summarize_view'),
]