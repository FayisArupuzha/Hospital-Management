from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name = 'index'),
    path('home/',views.home, name = 'home'),

    path('about/',views.about , name = 'about'),
    path('booking/',views.booking, name = 'booking'),
    path('department/',views.department, name ='department'),
    path('doctors/',views.doctor, name ='doctors'),
    path('contact/',views.contact, name ='contact'),
    path('carrer/',views.career, name ='career'),
    path('registration/',views.registration, name ='registration'),
    path('login/',views.login_user, name ='login_user'),
    path('logout/',views.logout, name ='logout'),









]
