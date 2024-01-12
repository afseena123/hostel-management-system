from django import forms

class BookingForm(forms.Form):
    booking_date = forms.DateField(label='Booking Date')
    vacate_date = forms.DateField(label='Vacate Date')
    

    customername = forms.CharField(label='customername')
    address = forms.CharField(label='Address')
    gender =forms.CharField(label='Gender')
    contact = forms.CharField(label='Contact')
    email = forms.EmailField(label='Email')