"""Checks of supplied foundation only; assessed TODOs are not called."""

from datetime import datetime

import pytest

from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)



def test_required_patientfields() -> None:
    """Verify required fields."""
    patients = [
        ('', 'bob dylan'),
        ('P2', ' '),
        (None, 'bob dylan'),
    ]
    for patient_id, patient_name in patients:
        with pytest.raises(ValueError):
            Patient(patient_id, patient_name)
    p1 = Patient('P1', 'bob dylan')
    assert p1.patient_id == 'P1' and p1.name == 'bob dylan'
    
def test_required_practitionerfields() -> None:
    """Verify required fields."""
    practitioners = [
        ('', 'Jared Smith', 'Proctologyst'),
        ('D2', ' ', 'Proctologyst'),
        ('D3', 'Jared Smith', ''),
        (None, 'Jared Smith', 'Proctologyst'),
    ]
    for practitioner_id, practitioner_name, specialty in practitioners:
        with pytest.raises(ValueError):
            Practitioner(practitioner_id, practitioner_name, specialty)
    d1 = Practitioner('D1', 'Jared Smith', 'Proctologyst')
    assert d1.practitioner_id == 'D1' and d1.name == 'Jared Smith' and d1.specialty == 'Proctologyst'
    
def invalid_appoint_constrction(patient, practitioner) -> None:
    """Verify required fields."""

    appointments = [
        ('', patient, practitioner, datetime(2026, 10, 1, 9)),
        ('A2', None, practitioner, datetime(2026, 10, 1, 9)),
        ('A3', patient, None, datetime(2026, 10, 1, 9)),
        ('A4', patient, practitioner, None),
    ]
    for appointment_id, patient_obj, practitioner_obj, date_time in appointments:
        with pytest.raises(ValueError):
            Appointment(appointment_id, patient_obj, practitioner_obj, date_time)
    test = Appointment('A1', patient, practitioner, datetime(2026, 10, 1, 9))
    assert test.appointment_id == 'A1' and test.patient == patient and test.practitioner == practitioner and test.date_time == datetime(2026, 10, 1, 9) and test.status == AppointmentStatus.SCHEDULED

def test_guarded_cancleation_appointment(patient, practitioner) -> None:
    """Verify required fields."""
    appointment1 = Appointment('A1', patient, practitioner, datetime(2026, 10, 1, 9), AppointmentStatus.CANCELLED)
    appointment2 = Appointment('A2', patient, practitioner, datetime(2026, 11, 1, 9), AppointmentStatus.COMPLETED)
    with pytest.raises(ValueError):
        appointment1.cancel()
        appointment2.cancel()
    assert appointment1.status == AppointmentStatus.CANCELLED and appointment2.status == AppointmentStatus.COMPLETED