
from datetime import timezone
from django.db import models
from django.contrib.auth.models import User




from django.shortcuts import render, redirect






class Hostel(models.Model):
    
   
    hostelname = models.CharField(max_length=255)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=23)
    num_of_beds = models.IntegerField()
    
    
    image = models.ImageField(upload_to='hostel_images/', null=True,blank=True)  # Default value when no image is provided
    

    def __str__(self):
        return self.hostelname
   






    
class RoomType(models.Model):
    roomtypeid = models.AutoField(primary_key=True)
    typename = models.CharField(max_length=255)

    def __str__(self):
        return self.typename

class Block(models.Model):
    blockid = models.AutoField(primary_key=True)
    blockname = models.CharField(max_length=255)
    noofrooms = models.PositiveIntegerField()

    def __str__(self):
        return self.blockname
class Room(models.Model):
    roomid = models.AutoField(primary_key=True)
    roomname = models.CharField(max_length=255)
    blockid = models.ForeignKey('Block', on_delete=models.CASCADE)
    roomtypeid = models.ForeignKey('RoomType', on_delete=models.CASCADE)
    facilities = models.TextField()
    noofbeds = models.PositiveIntegerField()

    def __str__(self):
        return self.roomname
    
class BedDetails(models.Model):
    bedid = models.IntegerField(primary_key=True)
    roomid = models.ForeignKey('Room', on_delete=models.CASCADE)
    bedname = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    

    def __str__(self):
        return f"{self.bedname} - {self.roomid}"


class RoomVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visit_date = models.DateField()
    visit_time = models.TimeField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE)  # Replace 'yourapp' with your actual app name
    purpose = models.TextField()
    
    def __str__(self):
        return f"{self.user.username} visiting {self.room.roomname} on {self.visit_date} at {self.visit_time}"


# models.py
from django.db import models

class HostelDetail(models.Model):
    # Your other fields

    class DistrictChoices(models.TextChoices):
        DISTRICT_1 = 'Malappuram', 'Malappuram'
        DISTRICT_2 = 'Calicut', 'Calicut'
        DISTRICT_3 = 'kasargod', 'Kasargod'
        District_4 = 'Kannoor' ,'kannoor'
        District_5 = 'Trivandrum' ,'Trivandrum'
        District_6 = 'Palakkad' ,'Palakkad'
        District_7= 'Ernamkulam','Ernamkulam'
        District_8='Pathanamthitta','Pathanamthitta'
        District_9 = 'Kollam' ,'Kollam'
        District_10 = 'Alappuzha' ,'Alappuzha'
        District_11 = 'Vayanad' ,'Vayanad'
        District_12 = 'Kottayam' ,'Kottayam'
        District_13 = 'Trissure' ,'Trissure'
        District_14 = 'Idukki' ,'Idukki'

        
        # Add other districts here...

    district = models.CharField(
        max_length=50,
        choices=DistrictChoices.choices,
        default=DistrictChoices.DISTRICT_1
    )
    hostelname=models.TextField()
    address=models.TextField()
    district=models.TextField()

