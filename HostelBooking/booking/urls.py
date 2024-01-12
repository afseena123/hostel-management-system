from . import views
from django.urls import path



urlpatterns = [
    path('bookingsdetails/', views.bookingsdetails, name='bookingsdetails'),
    path('check_availability/',views. check_availability,name= 'check_availability'),
    path('beddetails/<int:room_id>/', views.beddetails, name='beddetails'),
    
    # path('booknow/<int:room_id>/', views.booknow, name='booknow'),
    path('booknow/<int:room_id>/', views.booknow, name='booknow'),

    # path('booking/room_booking_payment/<int:booking_id>/', views.room_booking_payment, name='room_booking_payment'),
    
    
    
    
    path('booking/booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('payment/', views.payment, name='payment'),
  
]