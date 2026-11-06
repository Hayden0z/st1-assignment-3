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

#known and unknown lookups
def test_find_items_by_ID() -> None:
    """Verify required fields."""
    (data_store, patient_service, practitioner_service, appointment_service, patient, practitioner, appointment) = foundation()

    assert patient_service.find_patient("P1") is patient
    assert practitioner_service.find_practitioner("D1") is practitioner
    assert appointment_service.find_appointment("A1") is appointment
    

    #test service cancel retains history
def test_cancel_retains_history() -> None:
    """Verify required fields."""
    (data_store, patient_service, practitioner_service, appointment_service, patient, practitioner, appointment) = foundation()
    assert appointment_service.find_appointment("A1") is appointment
    assert appointment_service.cancel_appointment("A1")
    assert appointment_service.find_appointment("A1") is appointment
        
    #test complete cancleation rejected without change
def test_failed_cancel_retains_history(patient, practitioner) -> None:
    "Using local feilds"
    appointment1 = Appointment('A1', patient, practitioner, datetime(2026, 10, 1, 9),AppointmentStatus.COMPLETED)
    with pytest.raises(ValueError):
            appointment1.cancel()
    assert appointment1.appointment_id == 'A1' and appointment1.patient == patient and appointment1.practitioner == practitioner and appointment1.date_time == datetime(2026, 10, 1, 9) and appointment1.status == AppointmentStatus.COMPLETED

    #test failed bookings leave all recoreds unchaged
def test_failed_booking_datastore_unchanged() -> None:
    """Verify required fields."""
    (data_store, patient_service, practitioner_service, appointment_service, patient, practitioner, appointment) = foundation()
    
    with pytest.raises(ValueError):
                appointment2 = Appointment('A1', 'P1', 'D1', datetime(2026, 10, 1, 9))
    appointment1 = appointment_service.find_appointment("A1")
    assert appointment1.appointment_id == 'A1' and appointment1.patient == patient and appointment1.practitioner == practitioner and appointment1.date_time == datetime(2026, 10, 1, 9) and appointment1.status == AppointmentStatus.SCHEDULED


 #test canceled slot is free and patient conflict is not invented
def test_slot_free_once_cancled(patient, practitioner) -> None:
    "Using local feilds"
    
    appointment1 = Appointment('A1', patient, practitioner, datetime(2026, 10, 1, 9))
    appointment1.cancel()
    appointment2 = Appointment('A1', patient, practitioner, datetime(2026, 10, 1, 9))

    assert appointment2.appointment_id == 'A1' and appointment2.patient == patient and appointment2.practitioner == practitioner and appointment2.date_time == datetime(2026, 10, 1, 9) and appointment2.status == AppointmentStatus.SCHEDULED
    
