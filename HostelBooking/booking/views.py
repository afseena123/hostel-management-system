
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.forms import Form

from .models import Booking, Room
from django.shortcuts import render
from .models import Room, BedDetails  # Import your Room and BedDetails models

from django.shortcuts import render
from .models import Room, BedDetails

from django.shortcuts import render, get_object_or_404
from .models import Booking

from . models import RoomVisit

from hosteldetails. models import Room

from .models import Customer, RoomType,Hostel
from . models import Booking
from .models import BedDetails 
from .models import Payment
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
def check_availability(bedid,booking_date,vecate_date):
    avail_list=[]
    booking_list=booking.objects.filter(bedid=bedid)
    for booking in booking_list:
        if booking.booking_date > vecate_date or booking.vecate_date < vecate_date:
            avail_list.append(True)


        else:
            avail_list.append(False)
    return all(avail_list)


def bookingsdetails(request):
    bookings = Booking.objects.all()  # Fetch all bookings
    return render(request, 'booking_details.html', {'bookings': bookings})


def check_availability(request):
    # Fetching data from the database
    available_beds = BedDetails.objects.filter(availability=True)  # Fetch available beds

    # Filter available rooms based on criteria (for example, rooms with available beds)
    available_rooms = set()
    for bed in available_beds:
        available_rooms.add(bed.roomid)

    context = {
        'available_beds': available_beds,
        'available_rooms': available_rooms,
    }

    # Render a template with the fetched data
    return render(request, 'availability.html', context)


def beddetails(request, room_id):
    beds = BedDetails.objects.filter(roomid=room_id)  # Fetch beds related to the room_id

    context = {
                'beds': beds,
     }

    return render(request, 'bed_details.html', context)



# views.py
from django.shortcuts import render, redirect
from .models import BedDetails


   

def booknow(request, room_id):
    room = BedDetails.objects.filter(roomid=room_id).first()  # Get the first room details
    available_beds = BedDetails.objects.filter(roomid=room_id, availability=True)  # Get available beds for the room

    context = {
        'room': room,
        'available_beds': available_beds,
    }

    if request.method == 'POST':
        selected_bed_id = request.POST.get('selected_bed')  # Get the selected bed ID from the form

        
        return redirect('booking_confirmation.html')  # Replace 'booking_confirmation' with your confirmation URL

    return render(request, 'book_now.html', context)

def booking_confirmation(request):
    room = BedDetails.objects()
    bedid = BedDetails.objects()
    
    context = {
        'room': room,
        'bedid' :bedid, # Replace with your fetched room details or booking information
        # Add more context variables if needed for the confirmation message
    }

    return render(request, 'booking_confirmation.html', context)

from .models import BedDetails  # Import your BedDetails model

def booking_confirmation(request):
    all_rooms = BedDetails.objects.all()  # Fetch all BedDetails objects

    context = {
        'all_rooms': all_rooms,  # Pass the retrieved data to the context
        # Add more context variables if needed for the confirmation message
    }

    return render(request, 'booking_confirmation.html', context)


from django.shortcuts import render, redirect
from .models import BedDetails  # Import your BedDetails model or relevant models




from .models import Room, BedDetails  # Import your Room and BedDetails models

def booking_confirmation(request):
    # Assume the room_id and bed_id come from the request or another dynamic source
    room_id = request.GET.get('room_id')  # Get room_id from the query parameters (GET request)
    bed_id = request.GET.get('bed_id')    # Get bed_id from the query parameters (GET request)

    # Fetch room and bed objects based on room_id and bed_id
    room = get_object_or_404(Room, roomid=room_id)
    bed = get_object_or_404(BedDetails, bedid=bed_id)

    context = {
        'room': room,
        'bed': bed,
    }

    return render(request, 'booking_confirmation.html', context)




def booking_confirmation(request):
    # Retrieve room and bed details (Replace these with your actual logic to fetch data)
    room_id = 1  # Replace with actual room ID
    selected_bed_id = 1  # Replace with actual selected bed ID

    # Assuming you have retrieved room and bed details from your database
    room = {
        'roomid': room_id,
    }
    
    context = {
        'room': room,
        'selected_bed_id': selected_bed_id,
        # Add other relevant booking details to pass to the template
    }

    return render(request, 'booking_confirmation.html', context)
def payment(request):
    if request.method == 'POST':
        
        account_number = request.POST.get('account_number')
        name= request.POST.get('name')
        expiry_month = request.POST.get('expiry_month')
        cvv = request.POST.get('cvv')

        p=payment(
            user=request.user,
            account_number=account_number,
            name=name,
            expiry_month=expiry_month,
            cvv=cvv,

        )
        p.save()

        

    return render(request,'payment.html') 

# views.py


