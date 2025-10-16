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

    def doctor_info(self):
        return f"Dr. {self.name} {self.specialty}"


