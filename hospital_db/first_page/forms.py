from django import forms

from .models import Booking

class Dateinput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': Dateinput(),
        }

        labels = {
            "p_name": "Patient Name",
            "p_phone": "Patient Phone",
            "p_email": "Patient Email",
            "doc_name": "Doctor Name",
            "booking_date":"Booking Date",
            
        }
class CareerForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
