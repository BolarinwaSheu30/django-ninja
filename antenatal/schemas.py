"""
Schemas for the Antenatal Care API.
"""

# Import Python's date type.
from datetime import date

# Import Django Ninja's Schema.
from ninja import Schema


class AntenatalVisitCreateSchema(Schema):
    """
    Data required to create
    an antenatal visit.
    """

    # Pregnancy database ID.
    pregnancy_id: int

    # Date of the clinic visit.
    visit_date: date

    # Maternal weight in kilograms.
    weight_kg: float

    # Blood pressure reading.
    blood_pressure: str

    # Fetal heart rate.
    fetal_heart_rate: int

    # Maternal temperature in Celsius.
    temperature_c: float | None = None

    # Maternal pulse rate.
    pulse_rate: int | None = None

    # Fundal height in centimeters.
    fundal_height_cm: float | None = None

    # Whether fetal movement is present.
    fetal_movement_present: bool = True

    # Urine protein result.
    urine_protein: str = ""

    # Urine glucose result.
    urine_glucose: str = ""

    # Next clinic appointment date.
    next_appointment_date: date | None = None

    # Optional clinical notes.
    notes: str = ""


class AntenatalVisitResponseSchema(Schema):
    """
    Response returned after
    creating or retrieving a visit.
    """

    id: int

    # Human-friendly patient identifier.
    patient_id: str

    visit_date: date

    # Visit number assigned by the backend.
    visit_number: int

    weight_kg: float
    blood_pressure: str
    fetal_heart_rate: int

    temperature_c: float | None = None
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
    Lightweight schema used when
    listing antenatal visits.
    """

    id: int
    patient_id: str
    visit_number: int
    visit_date: date