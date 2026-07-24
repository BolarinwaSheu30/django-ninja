"""
Schemas for the Pregnancy API.
"""

from datetime import date

from ninja import Schema


class PregnancyCreateSchema(Schema):
    """
    Data required to register
    a new pregnancy.

    The backend calculates the
    Estimated Date of Delivery (EDD)
    and gestational age.
    """

    patient_id: int

    booking_date: date

    lmp: date

    gravida: int

    parity: int

    notes: str = ""


class PregnancyResponseSchema(Schema):
    """
    Detailed pregnancy information.

    Reserved for endpoints that return
    a Pregnancy object directly.
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
    Lightweight pregnancy information
    for list endpoints.
    """

    id: int

    patient_id: str

    booking_date: date

    edd: date

    gestational_age_weeks: int

    pregnancy_status: str

    @staticmethod
    def resolve_patient_id(obj):
        """
        Return the hospital patient ID.
        """

        return obj.patient.patient_id


class ErrorSchema(Schema):
    """
    Legacy error schema.

    This has been replaced by
    ErrorResponseSchema in
    config.common_schemas.
    """

    detail: str