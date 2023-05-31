from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse,HttpResponseRedirect
from .models import Department,Doctors,Booking
from .forms import BookingForm,CareerForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib import auth



# Create your views here.
def home(request):
    return render(request, 'home_page.html')

def about(request):
    return render(request,'about_page.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

    
    
    booking = BookingForm()
    form = {
        'form_dict' : booking
    }
    return render(request,'booking_page.html',form)

def department(request):
    dept = {
        'dept_name' : Department.objects.all()
    }
    return render(request,'department_page.html', dept)

def doctor(request):
    doc = {'doctors_dep' : Doctors.objects.all()}
    return render(request,'doctors_page.html', doc)

def contact(request):
    return render(request,'contact_page.html')

def career(request):
    form =CareerForm()
    context = {'form': form}


    return render(request,'career.html', context)

def registration(request):
    if request.method == 'POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        user_name =request.POST['user_name']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        

        if password1 == password2 and user_name != '':
            if User.objects.filter(username=user_name).exists():
                messages.add_message(request, messages.ERROR, 'user name is allreday taken ')
                return HttpResponseRedirect(reverse('registration'))
            else:

                user =User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.set_password(password1)
                user.save()
                print('user created')
                return redirect('login_user')
    
        else:
            messages.add_message(request, messages.ERROR, 'password not matching')
            return HttpResponseRedirect(reverse('registration'))
    else:
        return render(request,'registration.html')    

def login_user(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'invalid user name or password')
            return HttpResponseRedirect(reverse('login_user'))
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('index')

def index(request):
    return render(request,'index.html')                