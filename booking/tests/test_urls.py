from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import booking,show_bookings,car_return,AddCarCategory


class TestUrls(SimpleTestCase):

    def test_list_all_urls(self):
        url = reverse('show_bookings')
        self.assertEqual(resolve(url).func,show_bookings)

    def test_bookings(self):
        url = reverse('booking')
        self.assertEqual(resolve(url).func,booking)

    def test_show_bookings(self):
        url = reverse('show_bookings_number',args=['34'])
        self.assertEqual(url, '/show_bookings/34/')

    def test_car_return(self):
        url = reverse('car_return',args=['5'])
        self.assertEqual(url, '/car_return/5/')
    
    def test_AddCarCategory(self):
        url = reverse('create_booking')
        self.assertEqual(resolve(url).func.view_class,AddCarCategory)