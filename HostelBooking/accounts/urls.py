from django.urls import path,include
from .import views
urlpatterns = [  
    path('loadregister',views.loadregister,name='loadregister'),

    path('loadlogin',views.loadlogin,name='loadlogin'),
    
   
    path('loadregister1',views.loadregister1,name='loadregister1'),
    
    path('loadlogin1',views.loadlogin1,name='loadlogin1'),
    path('save_hostel_details',views. save_hostel_details,name='save_hostel_details'),
]

   

