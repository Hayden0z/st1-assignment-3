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
    Patient,
    Practitioner,
    AppointmentService,
]:
    """Create fresh registered participants and services for a supplied
    check.
    """
    data_store = SmartCareDataStore()
    patient = PatientService(data_store).register_patient('P1', 'bob dylan')
    practitioner = PractitionerService(
        data_store,
    ).register_practitioner('D1', 'Jared Smith', 'Proctologyst')
    return (data_store, patient, practitioner, AppointmentService(data_store))


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
    
def invalid_appoint_constrction() -> None:
    """Verify required fields."""
    data_store, patient, practitioner, appointment_service = foundation()
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