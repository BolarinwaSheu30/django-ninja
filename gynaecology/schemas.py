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

    # Patient database ID.
    patient_id: int

    # Consultation date.
    consultation_date: date

    # Type of consultation.
    consultation_type: str

    # Presenting complaint.
    presenting_complaint: str

    # Optional clinical details.
    history: str = ""
    examination_findings: str = ""
    diagnosis: str = ""
    treatment: str = ""
    follow_up_plan: str = ""
    notes: str = ""


class GynecologyConsultationResponseSchema(Schema):
    """
    Response returned after
    creating or retrieving a consultation.
    """

    id: int

    # Human-friendly patient ID.
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
    Lightweight schema used when
    listing consultations.
    """

    id: int
    patient_id: str
    consultation_date: date
    consultation_type: str