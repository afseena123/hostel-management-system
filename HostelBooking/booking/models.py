import django
from django.db import models
from hosteldetails.models import *
# Create your models here.
from django.contrib.auth.models import User

django.utils.timezone
    
    # Other fields for Customer model



   
   
    
    
class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    CUSTOMER_CATEGORY_CHOICES = [
        ('Student', 'Student'),
        ('Employee', 'Employee'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    customername = models.CharField(max_length=255)
    customerid = models.AutoField(primary_key=True)
      # Specify a default value directly in the model
    
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    customercategory = models.CharField(max_length=10, choices=CUSTOMER_CATEGORY_CHOICES)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.customername



class Booking(models.Model):
    
    
    bookingid = models.AutoField(primary_key=True)
    booking_date = models.DateField()
    vacate_date = models.DateField()
    customerid = models.ForeignKey('Customer', on_delete=models.CASCADE)
    bedid = models.ForeignKey('hosteldetails.BedDetails', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking #{self.bookingid} - {self.customerid.customername}"
    



class checkout(models.Model):
    chid = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    # country = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    onotes = models.CharField(max_length=200)
    towncity = models.CharField(max_length=100)
    postcodezip = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    checkoutdate = models.DateTimeField(default='2023-10-30')


class Payment(models.Model):
    pmid= models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

    account_number=models.CharField(max_length=255,default='5001')
    name=models.CharField(max_length=255)
    expiry_month=models.CharField(max_length=2)
    expiry_year=models.CharField(max_length=2)
    cvv=models.CharField(max_length=3)
    paymentdate=models.DateTimeField(default='2023-10-30')
    
