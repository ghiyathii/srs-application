# Generated by Django 4.2.2 on 2023-06-13 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Appointment_IP',
            new_name='Appointment_ID',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_time',
            new_name='Appointment_time',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Doctor_IP',
            new_name='Doctor_ID',
        ),
        migrations.RenameField(
            model_name='patinet',
            old_name='Patient_IP',
            new_name='Patient_ID',
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='patient_name',
            new_name='Patient_name',
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='Prescription_IP',
            new_name='Prescription_ID',
        ),
    ]