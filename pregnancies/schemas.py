"""
Schemas for the Pregnancy API.

Schemas define the structure of
incoming requests and outgoing responses.
"""

# Import Python's date type.
from datetime import date

# Import Django Ninja's Schema class.
from ninja import Schema


"""
Schema used when creating
a pregnancy record.
"""

class PregnancyCreateSchema(Schema):
    """
    Data required to register
    a new pregnancy.

    The backend will calculate
    the EDD and gestational age.
    """

    # Database ID of the patient.
    patient_id: int

    # Date of antenatal booking.
    booking_date: date

    # Last Menstrual Period.
    lmp: date

    # Number of pregnancies.
    gravida: int

    # Number of deliveries.
    parity: int

    # Current pregnancy status.
    

    # Optional notes.
    notes: str = ""

class PregnancyResponseSchema(Schema):
    """
    Schema returned when
    retrieving a pregnancy.
    """

    id: int

    patient_id: str

    booking_date: date
    lmp: date
    edd: date

    gestational_age_weeks: int

    gravida: int
    parity: int

    pregnancy_status: str

    notes: str

    @staticmethod
    def resolve_patient_id(obj):
        """
        Return the hospital patient ID
        instead of the database ID.
        """

        return obj.patient.patient_id

class PregnancyListSchema(Schema):
    """
    Lightweight schema for
    listing pregnancies.
    """

    id: int

    patient_id: str

    booking_date: date

    pregnancy_status: str

class ErrorSchema(Schema):
    """
    Standard error response.
    """

    detail: str