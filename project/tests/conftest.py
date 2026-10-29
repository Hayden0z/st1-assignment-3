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

@pytest.fixture
def patient() -> Patient:
    """Create a registered patient for use in tests."""
    data_store = SmartCareDataStore()
    return PatientService(data_store).register_patient('P1', 'Alex Example')

@ pytest.fixture
def practitioner() -> Practitioner: 
    """Create a registered practitioner for use in tests."""
    data_store = SmartCareDataStore()
    return PractitionerService(
        data_store,
    ).register_practitioner('D1', 'Taylor Example', 'General')

