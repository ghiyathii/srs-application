from django.db import models

class Patinet_Record(models.Model):
    Patient_ID = models.AutoField(primary_key=True)
    Patient_name = models.CharField(max_length=100)
    patient_address = models.CharField(max_length=100)
    patient_contact = models.CharField(max_length=100)
    patient_age = models.CharField(max_length=2)
    patient_gender = models.CharField(max_length=2)
    patient_medicalhistory = models.CharField(max_length=100)
    patient_insurance = models.CharField(max_length=100)
    prescription = models.CharField(max_length=100)
    class meta:
        db_table = 'Patinet_Record'

    def __str__(self):
        return self.Patient_ID


class Doctor_Record(models.Model):
    Doctor_ID = models.IntegerField(primary_key=True)
    Doctor_name = models.CharField(max_length=100)
    Doctor_address = models.CharField(max_length=100)
    Doctor_Connection = models.CharField(max_length=100)
    Doctor_Specialization = models.CharField(max_length=100)
    Doctor_Certificate = models.CharField(max_length=100)
    Doctor_availability = models.CharField(max_length=100)
    Doctor_Appointments = models.CharField(max_length=100)
    class meta:
        db_table = 'Doctor_Record'

    def __str__(self):
        return self.Doctor_ID

class Appointment_Schedulee(models.Model):
    Appointment_ID = models.IntegerField(primary_key=True)
    patient_name = models.CharField(max_length=100)
    patient_contact = models.CharField(max_length=100)
    Appointment_date = models.CharField(max_length=100)
    Appointment_time = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    Appointment_reason = models.CharField(max_length=100)
    Appointment_Status = models.CharField(max_length=100)
    class meta:
        db_table = 'Appointment_Schedulee'

    def __str__(self):
        return self.Appointment_ID



class Prescription_Record(models.Model):
    Prescription_ID = models.IntegerField(primary_key=True)
    Patient_name = models.CharField(max_length=100)
    Doctor_name = models.CharField(max_length=100)
    Prescription_date = models.CharField(max_length=100)
    Prescription_name = models.CharField(max_length=100)
    Prescription_dose = models.CharField(max_length=100)
    class meta:
        db_table = 'Prescription_Record'

    def __str__(self):
        return self.Prescription_ID 

