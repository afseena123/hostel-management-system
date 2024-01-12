from django.contrib import admin

# Register your models here.
from .models import Hosteldetails
from .models import Student

# Register your models here.
admin.site.register(Student)
# Register your models here.
admin.site.register(Hosteldetails)