# Hospital Patient Management
# Create a hospital management system that tracks doctors, patients, and appointments.

# Doctors can have specialties, and patients may have different ailments.
# Each appointment should store the doctor-patient relationship, along with the date and time.
# Add functionality for doctors' schedules and ensuring no double booking.

from datetime import datetime


class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.schedule = []  # List of appointment datetime objects

    def is_available(self, appointment_time):
        """Check if doctor is available at the given time."""
        return appointment_time not in self.schedule

    def add_appointment(self, appointment_time):
        """Add an appointment to the doctor's schedule."""
        if self.is_available(appointment_time):
            self.schedule.append(appointment_time)
            return True
        return False

    def __str__(self):
        return f"Dr. {self.name} {self.specialty}"


class Patient:
    def __init__(self, doctor, patient, appointment_time):
        self.doctor = doctor
        self.patient = patient
        self.appointment_time = appointment_time

    def __str__(self):
        return f"Appointment: {self.appointment_time.strftime('%Y-%m-%d %H:%M')} - {self.doctor} with {self.patient}"


class Appointment:
    def __init__(self, doctor, patient, appointment_time):
        self.doctor = doctor
        self.patient = patient
        self.appointment_time = appointment_time

    def __str__(self):
        return f"Appointment: {self.appointment_time.strftime('%Y-%m-%d %H:%M')} - {self.doctor} with {self.patient}"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = {}
        self.patients = {}
        self.appointments = {}

    def add_doctor(self, doctor):
        self.doctors[doctor.doctor_id] = doctor

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient


