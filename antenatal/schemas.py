"""
Schemas for the Antenatal Care API.
"""

from datetime import date

from ninja import Schema


class AntenatalVisitCreateSchema(Schema):
    """
    Data required to create
    an antenatal visit.
    """

    pregnancy_id: int

    visit_date: date

    weight_kg: float

    blood_pressure: str

    fetal_heart_rate: int

    temperature_c: float | None = None

    pulse_rate: int | None = None

    fundal_height_cm: float | None = None

    fetal_movement_present: bool = True

    urine_protein: str = ""

    urine_glucose: str = ""

    next_appointment_date: date | None = None

    notes: str = ""


class AntenatalVisitResponseSchema(Schema):
    """
    Detailed antenatal visit information.

    Reserved for endpoints that return
    an AntenatalVisit object directly.
    """

    id: int

    patient_id: str

    visit_date: date

    visit_number: int

    weight_kg: float

    blood_pressure: str

    fetal_heart_rate: int

    temperature_c: float |None = None

    pulse_rate: int | None = None

    fundal_height_cm: float | None = None

    fetal_movement_present: bool

    urine_protein: str

    urine_glucose: str

    next_appointment_date: date | None = None

    notes: str

    @staticmethod
    def resolve_patient_id(obj):
        """
        Return the hospital patient ID.
        """

        return obj.pregnancy.patient.patient_id


class AntenatalVisitListSchema(Schema):
    """
    Lightweight antenatal visit
    information for list endpoints.
    """

    id: int

    patient_id: str

    visit_number: int

    visit_date: date

    blood_pressure: str

    fetal_heart_rate: int

    next_appointment_date: date | None = None

    @staticmethod
    def resolve_patient_id(obj):
        """
        Return the hospital patient ID.
        """

        return obj.pregnancy.patient.patient_id