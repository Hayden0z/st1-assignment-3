"""Checks of supplied foundation only; assessed TODOs are not called."""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

def foundation() -> tuple[
    SmartCareDataStore,
    PatientService,
    PractitionerService,
    Patient,
    Practitioner,
    AppointmentService,
]:
    """Create fresh registered participants and services for a supplied
    check.
    """
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)
    patient = patient_service.register_patient('P1', 'Alex Example')
    practitioner = practitioner_service.register_practitioner('D1', 'Jared Smith', 'Proctologyst')
    appointment = appointment_service.book_appointment('A1', 'P1', 'D1', datetime(2026, 10, 1, 9))
    # return (data_store, patient_service, practitioner_service, appointment_service, patient, practitioner)
    return (data_store, patient_service, practitioner_service, appointment_service, patient, practitioner, appointment)

def test_find_patientfield_by_ID() -> None:
    """Verify required fields."""
    (data_store, patient_service, practitioner_service, appointment_service, patient, practitioner, appointment) = foundation()

    assert patient_service.find_patient("P1") is patient
    
def test_find_practitionerfield_by_ID() -> None:
    (data_store, patient_service, practitioner_service, appointment_service, patient, practitioner, appointment) = foundation()
    assert practitioner_service.find_practitioner("D1") is practitioner
    
def test_find_appointmentfield_by_ID() -> None:
    (data_store, patient_service, practitioner_service, appointment_service, patient, practitioner, appointment) = foundation()
    assert appointment_service.find_appointment("A1") is appointment
    # 
    #kown and unknown lookups
    #test servuce cancle retains history
    #test complete cancleation rejected without change
    #test failed bookings leave all recoreds unchaged
    #test duplicate records and wrong store objects
    #test cancled slot is free and patient conflict is not invented