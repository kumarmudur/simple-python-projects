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
    def __init__(self, patient_id, name, ailment):
        self.patient_id = patient_id
        self.name = name
        self.ailment = ailment

    def __str__(self):
        return f"{self.name} (Ailment: {self.ailment}"


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

    def book_appointment(self, doctor_id, patient_id, appointment_time):
        """Book an appointment if doctor is available."""
        doctor = self.doctors.get(doctor_id)
        patient = self.patients.get(patient_id)

        if not doctor or not patient:
            print("Invalid doctor or patient ID.")
            return

        if doctor.is_available(appointment_time):
            doctor.add_appointment(appointment_time)
            appointment = Appointment(doctor, patient, appointment_time)
            self.appointments.append(appointment)
            print(f"✅ Appointment booked successfully:\n{appointment}")
        else:
            print(f"❌ Doctor {doctor.name} is not available at {appointment_time}.")

    def view_doctor_schedule(self, doctor_id):
        doctor = self.doctors.get(doctor_id)
        if not doctor:
            print("Doctor not found.")
            return

        print(f"\n📅 Schedule for {doctor.name}:")
        if not doctor.schedule:
            print("No appointments scheduled.")
        else:
            for time in sorted(doctor.schedule):
                print(f" - {time.strftime('%Y-%m-%d %H:%M')}")

    def list_appointments(self):
        print(f"\nAll Appointments at {self.name}:")
        if not self.appointments:
            print("No appointments booked yet.")
        else:
            for appointment in self.appointments:
                print(appointment)


# Example usage
if __name__ == "__main__":
    hospital = Hospital("CityCare Hospital")

    print(hospital.name)

    # Add doctors
    d1 = Doctor(1, "Alice Smith", "Cardiology")
    d2 = Doctor(2, "Bob Johnson", "Neurology")
    hospital.add_doctor(d1)
    hospital.add_doctor(d2)

    # App patients
    p1 = Patient(101, "John Doe", "Chest Pain")
    p2 = Patient(102, "Jane Roe", "Headache")
    hospital.add_patient(p1)
    hospital.add_patient(p2)

    # Book appointments
    appt_time1 = datetime(2025, 10, 16, 10, 0)
    appt_time2 = datetime(2025, 10, 16, 10, 0)  # same time (to test double booking)
    appt_time3 = datetime(2025, 10, 16, 11, 0)

    # View schedules
    hospital.view_doctor_schedule(1)
    hospital.view_doctor_schedule(2)

    # List all appointments
    hospital.list_appointments()