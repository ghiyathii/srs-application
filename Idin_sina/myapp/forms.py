from django import forms
from .models import Patinet, Doctor, Appointment, Prescription

class PatinetForm(forms.ModelForm):
    class Meta:
        model = Patinet
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'