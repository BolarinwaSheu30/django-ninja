"""
Schemas for the Postnatal Care API.
"""

from datetime import date

from ninja import Schema


class PostnatalVisitCreateSchema(Schema):
    """
    Data required to create
    a postnatal visit.
    """

    # Delivery database ID.
    delivery_id: int

    # Visit date.
    visit_date: date

    # Maternal observations.
    blood_pressure: str
    temperature_c: float
    pulse_rate: int

    # Lochia assessment.
    lochia: str = ""

    # Breastfeeding status.
    breastfeeding_status: str

    # Wound healing assessment.
    wound_healing: str = ""

    # Baby assessment.
    baby_weight_kg: float
    feeding_well: bool = True
    immunization_given: bool = False

    # Family planning counseling.
    family_planning_counseled: bool = False

    # Next appointment.
    next_appointment_date: date | None = None

    # Additional notes.
    notes: str = ""


class PostnatalVisitResponseSchema(Schema):
    """
    Response returned after
    creating or retrieving a visit.
    """

    id: int

    # Human-friendly patient ID.
    patient_id: str

    visit_date: date
    visit_number: int

    blood_pressure: str
    temperature_c: float
    pulse_rate: int

    lochia: str
    breastfeeding_status: str
    wound_healing: str

    baby_weight_kg: float
    feeding_well: bool
    immunization_given: bool

    family_planning_counseled: bool
    next_appointment_date: date | None = None

    notes: str

    @staticmethod
    def resolve_patient_id(obj):
        """
        Return the hospital patient ID.
        """

        return (
            obj.delivery.pregnancy.patient.patient_id
        )


class PostnatalVisitListSchema(Schema):
    """
    Lightweight schema used when
    listing postnatal visits.
    """

    id: int
    patient_id: str
    visit_number: int
    visit_date: date
    breastfeeding_status: str