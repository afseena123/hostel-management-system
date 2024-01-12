from django.shortcuts import render
from django.shortcuts import get_object_or_404


from django.shortcuts import render
from hosteldetails.models import Hostel
from booking.models import Customer,Booking
from .models import Hosteldetails
# views.py

from django.http import HttpResponseRedirect, JsonResponse

def adminpage(request):
    return render(request,'admin.html')


def get_hostel_list(request):
    hostels = Hostel.objects.all()
    return render(request, 'hostellist1.html', {'hostels': hostels})
# views.py

from django.shortcuts import render, redirect


from django.shortcuts import render, redirect


def HostelSubmission(request):
    if request.method == 'POST':
        hostel_name = request.POST.get('hostel_name')
        licence_number = request.POST.get('licence_number')
        owner_name = request.POST.get('owner_name')
        address = request.POST.get('address')

        # Create a new Hostel object and assign values to its fields
        hostel = Hostel()
        hostel.hostel_name = hostel_name
        hostel.licence_number = licence_number
        hostel.owner_name = owner_name
        hostel.address = address
        hostel.approved = False  # Newly submitted hostels are not approved by default
        hostel.save()
        
        return redirect('submission_success')
    return render(request, 'submit_hostel.html')


def AdminApproval(request):
    if request.user.is_superuser:  # Assuming superuser is the admin
        unapproved_hostels = Hosteldetails.objects.filter(approved=False)
        return render(request, 'admin_approval.html', {'unapproved_hostels': unapproved_hostels})
    else:
        # Redirect or display message for unauthorized access
        pass


from django.shortcuts import render, get_object_or_404
from .models import Hosteldetails

def approve_hostel(request, hostel_id):
    hostel = get_object_or_404(Hosteldetails, id=hostel_id)
    hostel.approved = True
    hostel.save()

    # Fetch the approved hostel details
    approved_hostel = Hosteldetails.objects.get(id=hostel_id)

    # Render the approved_hostel_details.html template with the hostel details
    return render(request, 'approved_hostel_details.html', {'hostel': approved_hostel})

from django.shortcuts import render, get_object_or_404, redirect





from .models import Student

from django.shortcuts import render
from .models import Student

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        aadhar_number = request.POST.get('aadhar_number')
    

        
        
        new_student = Student(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            email=email,
            phone_number=phone_number,
            address=address,
            aadhar_number=aadhar_number,
            
        )
        new_student.save()
        # Redirect to the view page after adding the student
        return redirect('view_students')
    else:
        return render(request, 'add_student.html')


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        # Retrieve form data for updating the student
        student.first_name = request.POST.get('first_name')
                                                          
        student.last_name = request.POST.get('last_name')
        student.date_of_birth = request.POST.get('date_of_birth')
        student.email = request.POST.get('email')
        student.aadhar_number=request.POST.get('aadhar_number')

        # Update other fields similarly
        student.save()
        # Redirect to the view page after editing the student
        return redirect('view_students')
    else:
        return render(request, 'edit_student.html', {'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        # Logic to handle deletion confirmation
        student.delete()
        # Redirect to the view page after deleting the student
        return redirect('view_students')
    else:
        return render(request, 'delete_student.html', {'student': student})
