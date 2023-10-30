from django.test import TestCase,Client
from django.urls import reverse
from booking.models import BookingModel,CarCategory
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.show_bookings = reverse('show_bookings')
        self.booking = reverse('booking')
        self.car_return = reverse('car_return')

    def test_show_bookings_view(self):
        response = self.client.get(self.show_bookings)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'show_booking.html')

    def test_bookings_view(self):

        response = self.client.get(self.booking)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'booking.html')

    def test_car_return_view(self):

        response = self.client.get(self.car_return)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'success.html')