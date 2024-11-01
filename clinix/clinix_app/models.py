from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brith_date = models.DateField()
    allergies = models.TextField()
    medical_history = models.TextField()
    phone = models.CharField(max_length=15)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)

class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='medications/')

class MedicationSchedule(models.Model):
    TIME_CHOICES = [
        ('MORNING', 'Morning'),
        ('AFTERNOON', 'Afternoon'),
        ('EVENING', 'Evening'),
        ('NIGHT', 'Night'),
    ]
    TIME_WHEN_CHOICES = [
        ('BEFORE', 'Before'),
        ('AFTER', 'After'),
        ('WITH', 'With'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.CharField(max_length=10, choices=TIME_CHOICES)
    time_when = models.CharField(max_length=10, choices=TIME_WHEN_CHOICES)
    dosage = models.CharField(max_length=100)

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

