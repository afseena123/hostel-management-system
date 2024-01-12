from django.contrib import admin
from .models import Customer
from .models import Payment
from .models import Booking
from .models import checkout

# Register your models here.
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Booking)
admin.site.register(checkout)