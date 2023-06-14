from django.shortcuts import render
from .models import Patinet_Record, Doctor_Record, Appointment_Schedulee, Prescription_Record

def main_menu(request):
    return render(request, 'main_menu.html')

def Patinet_Record(request):
    Patinet_Record = Patinet.objects.all()
    return render(request, 'Patinet_list.html', {'Patinet': Patinet_Record})

def Doctor_Record(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': Doctor_Record})

def Appointment_Schedulee(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': Appointment_Schedulee})

def Prescription_Record(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescription_list.html', {'prescriptions': Prescription_Record})

def patient_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        Patients = Patient.objects.filter(Patient_name__icontains=search_query)
        return render(request, 'patient_search_results.html', {'patients': Patients})
    return render(request, 'patient_search.html')

def doctor_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        doctors = Doctor.objects.filter(Doctor_name__icontains=search_query)
        return render(request, 'doctor_search_results.html', {'doctors': doctors})
    return render(request, 'doctor_search.html')

def appointment_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        appointments = Appointment.objects.filter(patient_name__icontains=search_query)
        return render(request, 'appointment_search_results.html', {'appointments': appointments})
    return render(request, 'appointment_search.html')

def prescription_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        prescriptions = Prescription.objects.filter(patient_name__icontains=search_query)
        return render(request, 'prescription_search_results.html', {'prescriptions': prescriptions})
    return render(request, 'prescription_search.html')