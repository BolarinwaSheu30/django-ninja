"""
Schemas for the Gynaecology API.
"""

from datetime import date

from ninja import Schema


class GynecologyConsultationCreateSchema(Schema):
    """
    Data required to create
    a gynaecology consultation.
    """

    patient_id: int

    consultation_date: date

    consultation_type: str

    presenting_complaint: str

    history: str = ""

    examination_findings: str = ""

    diagnosis: str = ""

    treatment: str = ""

    follow_up_plan: str = ""

    notes: str = ""


class GynecologyConsultationResponseSchema(Schema):
    """
    Detailed consultation information.

    Reserved for endpoints that return
    a GynecologyConsultation object directly.
    """

    id: int

    patient_id: str

    consultation_date: date

    consultation_type: str

    presenting_complaint: str

    history: str

    examination_findings: str

    diagnosis: str

    treatment: str

    follow_up_plan: str

    notes: str

    @staticmethod
    def resolve_patient_id(obj):
        """
        Return the hospital patient ID.
        """

        return obj.patient.patient_id


class GynecologyConsultationListSchema(Schema):
    """
    Lightweight consultation
    information for list endpoints.
    """

    id: int

    patient_id: str

    consultation_date: date

    consultation_type: str

    diagnosis: str

    @staticmethod
    def resolve_patient_id(obj):
        """
        Return the hospital patient ID.
        """

        return obj.patient.patient_id