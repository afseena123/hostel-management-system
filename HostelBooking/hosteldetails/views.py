from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render

from .models import BedDetails, Hostel, Room, RoomType

# Create your views here.
def loadindex(request):
    return render(request,'index.html')

def next(request):
    return render(request,'next.html')
def hostelowner(request):
    return render(request,'owner.html')

from django.shortcuts import render
# from .models import Hostel, Room

from django.shortcuts import render
# from .models import Hostel, Block, Room
from django.shortcuts import render
from .models import RoomVisit
from .models import HostelDetail


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import RoomVisit
@login_required
def schedule_room_visit(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customername')
        visit_date = request.POST.get('visit_date')
        room_id = request.POST.get('room_id')  # Assuming room_id is sent from the form
        purpose = request.POST.get('purpose')

        room_visit = RoomVisit.objects.create(
            visit_date=visit_date,
            room_id=room_id,
            purpose=purpose,
            user=request.user  # Assign the logged-in user to the RoomVisit instance
        )
        # If you want to store the customer_name without a field in the model:
        # room_visit.customer_name = customer_name
        room_visit.save()

        # Add any additional logic here

    return render(request, 'schedule_room_visit.html')


from django.shortcuts import render
from .models import RoomVisit  # Import your RoomVisit model

def scheduled_visits(request):
    scheduled_visits = RoomVisit.objects.all()  # Fetch all scheduled visits
    return render(request, 'scheduled_visits.html', {'scheduled_visits': scheduled_visits})
def create_hostel(request):
    if request.method == 'POST':
        hostelname = request.POST['hostelname']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        num_of_beds = request.POST['num_of_beds']
        image = request.FILES['image']  # Get the uploaded image file

        # Create a Hostel instance and save it to the database
        hostel = Hostel.objects.create(
            hostelname=hostelname,
            address=address,
            phone=phone,
            email=email,
            num_of_beds=num_of_beds,
            image=image  # Assign the uploaded image to the 'image' field
        )
        return redirect('rooms.html')  # Replace 'success_page' with your success page URL or name

    return render(request, 'hostel.html')
# views.py


def search_by_district(request):
    if request.method == 'POST':
        district_query = request.POST.get('district')  # Assuming the district value is obtained from a form input

        # Search for hostels based on the district
        hostels = HostelDetail.objects.filter(district__icontains=district_query)

        return render(request, 'search_results.html', {'hostels': hostels})

    return render(request, 'search_hostel.html')
