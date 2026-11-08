"""Stage 9 contracts for pure collection processing."""


from datetime import datetime

from smartcare.domain import Appointment, AppointmentStatus


def appointment_sort_key(appointment: Appointment) -> tuple[datetime, str]:
    return(appointment.date_time, appointment.appointment_id)    


def select_appointments(
    appointments: list[Appointment],
    practitioner_id: str,
    status: AppointmentStatus | None = None,
) -> list[Appointment]:

    results = []

    for appointoment in appointments:
        if appointoment.practitioner.practitioner_id == practitioner_id:

            if status is None or appointoment.status == status:
                results.append(appointoment)

    return sorted(results, key=appointment_sort_key)
    
  
