from django.urls import path
from . import views

urlpatterns = [
    path('main_menu/', views.main_menu, name='main_menu'),
    path('patient/search/', views.patient_search, name='patients'),
    path('doctor/search/', views.doctor_search, name='doctors'),
    path('prescription/search/', views.prescription_search, name='prescriptions'),
    path('appointment/search/', views.appointment_search, name='appointments'),
    path('Patinet/Record/', views.Patinet_Record, name='Patinet'),
    path('doctor/records/', views.Doctor_Record, name='doctors'),
    path('Prescription/Record/', views.Prescription_Record, name='prescriptions'),
    path('Appointment/Schedulee/', views.Appointment_Schedulee, name='appointments'),
]
