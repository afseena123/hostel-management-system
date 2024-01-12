from django.urls import path
from . import views

urlpatterns = [  
     path('',views.loadindex,name='loadindex'),
     path('next',views.next,name='next'),
     path('schedule-room-visit/', views.schedule_room_visit, name='schedule_room_visit'),
     path('hostelowner',views.hostelowner,name='hostelowner'),
     path('scheduled-visits/', views.scheduled_visits, name='scheduled_visits'),
     path('search/', views.search_by_district, name='search_by_district'),
]