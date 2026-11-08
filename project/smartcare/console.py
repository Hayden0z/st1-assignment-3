"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)
data_store = SmartCareDataStore()
patientService = PatientService(data_store)
practitionerService = PractitionerService(data_store)
appointmentService = AppointmentService(data_store)

def parse_date_time(text: str) -> datetime:
    """Parse YYYY-MM-DD HH:MM; raise ValueError for invalid input."""
    if (
        not isinstance(text, str)
        or re.fullmatch(
            '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', text
        ) is None
    ):
        raise ValueError('Use date/time format YYYY-MM-DD HH:MM')
    try:
        return datetime.strptime(text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError(
            'Invalid calendar date/time; use YYYY-MM-DD HH:MM',
        ) from None


def format_appointment(appointment: Appointment) -> str:
    """Return readable synthetic appointment details without changing
    state.
    """
    return (
        f'{appointment.appointment_id}: '
        f'{appointment.patient.patient_id} with '
        f'{appointment.practitioner.practitioner_id}, '
        f'{appointment.date_time:%Y-%m-%d %H:%M}, {appointment.status.value}'
    )


def run_demo() -> None:
    """Demonstrate supplied registration and booking using synthetic
    records.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    try:
        appointments.book_appointment(
            'A1',
            'P1',
            'DR1',
            parse_date_time('2026-10-01 09:00'),
        )
        print(format_appointment(appointments.find_appointment('A1')))
    except (ValueError, LookupError) as error:
        print(f'Error: {error}')
    print('Session-only data: records are lost on exit.')


def run_menu() -> None:

    while True:
        
     print("Choose an option from the following menu: ")
     print()
     print("[1] - Register patient")
     print("[2] - Find patient")
     print("[3] - Register practitioner") 
     print("[4] - Find practitioner")
     print("[5] - Book appointment")
     print("[6] - Cancel appointment")
     print("[7] - Find appointment")
     print("[8] - List practitioner appointments")
     print("[0] - Exit")
     print()
     print("******************************************")
     print()
     choice = input("Select 1, 2, 3, 4, 5, 6, 7, 8 or 0: ")
     try:

        if choice == "1":
         print("enter Patient ID and Name")
         patient_id = input("enter Patient ID:")
         name = input("enter Patient name: ")
         patient = patientService.register_patient(patient_id,name)
         print("patient successfulley regristed")
         print(patient)

        
        elif choice == "2":
         print("enter Patient ID")
         patient_id = input("Patient ID:")
         patient = patientService.find_patient(patient_id)
         print("patient found")
         print(patient) 

        elif choice == "3":
         print("enter Practitioner ID,Name and Specialty")
         practitioner_id = input("enter practitioner ID: ")
         name = input("enter practitioner name:")
         specialty = input("enter work area Specialty") 
         print("patient successfulley regristed")
         practitionerService.register_practitioner(practitioner_id,name,specialty) 

        
        elif choice == "4":
         print("enter Practitioner ID ")
         practitioner_id = input("P ID:")
         practitioner = practitionerService.find_practitioner(practitioner_id)
         print("practitioner found")
         print(practitioner) 


        elif choice == "5":
         print("Enter appioment details ")
         appointment_id = input("Appointment ID:")
         patient_id = input("Patient ID:")
         practitioner_id = input("Practitioner ID:")
         date_time = input("Date/time (YYYY-MM-DD HH:MM):")

         appointment = appointmentService.book_appointment(appointment_id,patient_id,practitioner_id,parse_date_time(date_time))
               
         print("Appointment booked successfully.")
         print(appointment)

         
        elif choice == "6":
         print("Enter appioment ID ")
         appointment_id = input("Appointment ID:")

         appointment = appointmentService.cancel_appointment(appointment_id)

         print("Appointment successfully Canclled .")
         print(appointment)

        
        elif choice == "7":
         print("enter appioment ID ")
         appointment_id = input("Appointment ID:")
         appointment = appointmentService.find_appointment(appointment_id)
         print("appioment found")
         print(appointment) 
    
        elif choice == "8":
           print("Enter Practitioner ID")

           practitioner_id = input("Practitioner ID: ")

           status = input("Status filter (scheduled/cancelled/completed, blank = all): ")
           if status == "":status = None
           
           elif status == "scheduled":
              status = AppointmentStatus.SCHEDULED
           
           elif status == "cancelled":
              status = AppointmentStatus.CANCELLED
           
           elif status == "completed":
              status = AppointmentStatus.COMPLETED
           else:
              raise ValueError("Status must be scheduled, cancelled or completed")
           
           appointments = (appointmentService.list_practitioner_appointments(practitioner_id,status,))
           if len(appointments) == 0:
              print("No appointments found.")
           else:
            for appointment in appointments:
               print(appointment)

        elif choice == "0":  
         print ("Thanks for using the program.") 
         break
    
    
    
    
        else:
            print("Please enter 1,2,3,4,5,6,7,8 or 0 only")
    
     except ValueError as error:
      print("Issue dected", error)

     except LookupError as error:
           print("Issue dected", error)



    """Stage 9: implement the register/find/book/cancel/list/exit menu.

    Call services, recover from expected input errors, and keep this
    session's data until exit. main.py reports the incomplete menu
    without crashing.
    """
    
