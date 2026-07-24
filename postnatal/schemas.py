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

    delivery_id: int

    visit_date: date

    blood_pressure: str

    temperature_c: float

    pulse_rate: int

    lochia: str = ""

    breastfeeding_status: str

    wound_healing: str = ""

    baby_weight_kg: float

    feeding_well: bool = True

    immunization_given: bool = False

    family_planning_counseled: bool = False

    next_appointment_date: date | None = None

    notes: str = ""


class PostnatalVisitResponseSchema(Schema):
    """
    Detailed postnatal visit information.

    Reserved for endpoints that return
    a PostnatalVisit object directly.
    """

    id: int

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

        return obj.delivery.pregnancy.patient.patient_id


class PostnatalVisitListSchema(Schema):
    """
    Lightweight postnatal visit
    information for list endpoints.
    """

    id: int

    patient_id: str

    visit_number: int

    visit_date: date

    breastfeeding_status: str

    next_appointment_date: date | None = None

    @staticmethod
    def resolve_patient_id(obj):
        """
        Return the hospital patient ID.
        """

        return obj.delivery.pregnancy.patient.patient_id