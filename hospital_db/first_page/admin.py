from django.contrib import admin
from .models import Department,Doctors,Booking

# Register your models here.
class AdminDepartment(admin.ModelAdmin):
    list_display = ('dep_name' , 'dep_dsc')
admin.site.register(Department,AdminDepartment)

admin.site.register(Doctors)

class AdminBooking(admin.ModelAdmin):
    list_display = ('p_name','p_phone','p_email','doc_name','booking_date','booked_on')

admin.site.register(Booking,AdminBooking)


