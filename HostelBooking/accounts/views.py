from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


    # views.py


# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def loadregister(request):
    if request.method == "POST":
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        email = request.POST.get('email')
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        cpwd = request.POST.get('cpassword')

        if pwd == cpwd:
            if User.objects.filter(username=un).exists():
                messages.error(request, "Username already taken!")
                return redirect("register")  # Replace "register" with your registration URL name
            elif User.objects.filter(email=email).exists():
                messages.error(request, "This email is already taken!")
                return redirect("register")  # Replace "register" with your registration URL name
            else:
                new_user = User.objects.create_user(first_name=fn, last_name=ln, email=email, username=un, password=pwd)
                new_user.save()
                messages.success(request, "Registration successful! Please login.")
                return redirect("login")  # Replace "login" with your login URL name
        else:
            messages.error(request, "Password does not match!")
            return redirect("loadlogin")  # Replace "register" with your registration URL name

    return render(request, 'register.html')  # Render the registration page

# Then, in your urls.py file, you can map this view function to a URL:
# For example:
# path('register/', register_user, name='register'),

def loadlogin(request): 
    if request.method=="POST":
        un=request.POST["username"]
        pwd=request.POST["password"]
        # print(un)
        # print(pwd)
        # fetching
        user=auth.authenticate(username=un,password=pwd)
        print(user)
        if user is not None:
            # print("hai")
            auth.login(request,user)
            return redirect('check_availability')
        else:
           
            messages.info(request,'Data is Invalid!!!!!')
            return redirect('loadlogin')
    else:           
        return render(request,'login.html')
    


def loadregister1(request):
    if request.method == "POST":
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        email = request.POST.get('email')
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        cpwd = request.POST.get('cpassword')

        if pwd == cpwd:
            if User.objects.filter(username=un).exists():
                messages.error(request, "Username already taken!")
                return redirect("register1")  # Replace "register" with your registration URL name
            elif User.objects.filter(email=email).exists():
                messages.error(request, "This email is already taken!")
                return redirect("register1")  # Replace "register" with your registration URL name
            else:
                new_user = User.objects.create_user(first_name=fn, last_name=ln, email=email, username=un, password=pwd)
                new_user.save()
                messages.success(request, "Registration successful! Please login.")
                return redirect("login1")  # Replace "login" with your login URL name
        else:
            messages.error(request, "Password does not match!")
            return redirect("loadlogin1")  # Replace "register" with your registration URL name

    return render(request, 'register1.html')  # Render the registration page

# Then, in your urls.py file, you can map this view function to a URL:
# For example:
# path('register/', register_user, name='register'),

def loadlogin1(request): 
    if request.method=="POST":
        un=request.POST["username"]
        pwd=request.POST["password"]
        # print(un)
        # print(pwd)
        # fetching
        user=auth.authenticate(username=un,password=pwd)
        print(user)
        if user is not None:
            # print("hai")
            auth.login(request,user)
            return redirect('check_availability')
        else:
           
            messages.info(request,'Data is Invalid!!!!!')
            return redirect('loadlogin1')
    else:           
        return render(request,'login1.html')
    










def save_hostel_details(request):
    if request.method == "POST":
        building_license = request.POST['building_license']
        adhar_card = request.POST['adhar_card']
        hostel_address = request.POST['hostel_address']
        place = request.POST['place']
        pincode = request.POST['pincode']
        room_details = request.POST['room_details']

        # Process the form data (without saving to a model)
        # You can perform any action you want with this data

        # For example, printing the data to the console
        print("Building License:", building_license)
        print("Adhar Card:", adhar_card)
        print("Hostel Address:", hostel_address)
        print("Place:", place)
        print("Pincode:", pincode)
        print("Room Details:", room_details)

        # Redirect to a success page or any other page as needed
        return redirect('success_page.html')  # Replace 'success_page' with your actual success page URL or name
    else:
        return render(request, 'hostel_details.html')
