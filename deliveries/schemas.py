"""
Schemas for the Delivery API.
"""

from datetime import datetime

from ninja import Schema


class DeliveryCreateSchema(Schema):
    """
    Data required to record a delivery.
    """

    # Pregnancy database ID.
    pregnancy_id: int

    # Date and time of delivery.
    delivery_datetime: datetime

    # Mode of delivery.
    mode_of_delivery: str

    # Baby sex.
    baby_sex: str

    # Birth weight in kilograms.
    birth_weight_kg: float

    # Apgar score at 1 minute.
    apgar_1_min: int

    # Apgar score at 5 minutes.
    apgar_5_min: int

    # Baby status.
    baby_status: str

    # Estimated blood loss in mL.
    estimated_blood_loss_ml: int

    # Maternal complications.
    maternal_complications: str = ""

    # Additional notes.
    notes: str = ""


class DeliveryResponseSchema(Schema):
    """
    Response returned after
    creating or retrieving a delivery.
    """

    id: int

    # Human-friendly patient ID.
    patient_id: str

    delivery_datetime: datetime
    mode_of_delivery: str
    baby_sex: str
    birth_weight_kg: float
    apgar_1_min: int
    apgar_5_min: int
    baby_status: str
    estimated_blood_loss_ml: int
    maternal_complications: str
    notes: str

    @staticmethod
    def resolve_patient_id(obj):
        """
        Return the hospital patient ID.
        """

        return obj.pregnancy.patient.patient_id


class DeliveryListSchema(Schema):
    """
    Lightweight schema used when
    listing deliveries.
    """

    id: int
    patient_id: str
    delivery_datetime: datetime
    mode_of_delivery: str
    baby_status: str