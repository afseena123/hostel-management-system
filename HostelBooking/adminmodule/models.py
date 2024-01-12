from django.db import models

# Create your models here.
from django.db import models

class Hosteldetails(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('dormitory', 'Dormitory'),
        
    ]

    hostel_name = models.CharField(max_length=100)
    licence_number = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.hostel_name
from django.db import models

class Student(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    aadhar_number = models.CharField(max_length=12, unique=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
