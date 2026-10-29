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