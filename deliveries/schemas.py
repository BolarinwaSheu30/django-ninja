"""
Schemas for the Delivery API.
"""

from datetime import datetime

from ninja import Schema


class DeliveryCreateSchema(Schema):
    """
    Data required to record
    a delivery.
    """

    pregnancy_id: int

    delivery_datetime: datetime

    mode_of_delivery: str

    baby_sex: str

    birth_weight_kg: float

    apgar_1_min: int

    apgar_5_min: int

    baby_status: str

    estimated_blood_loss_ml: int

    maternal_complications: str = ""

    notes: str = ""


class DeliveryResponseSchema(Schema):
    """
    Detailed delivery information.

    Reserved for endpoints that return
    a Delivery object directly.
    """

    id: int

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
    Lightweight delivery information
    for list endpoints.
    """

    id: int

    patient_id: str

    delivery_datetime: datetime

    mode_of_delivery: str

    baby_sex: str

    baby_status: str

    @staticmethod
    def resolve_patient_id(obj):
        """
        Return the hospital patient ID.
        """

        return obj.pregnancy.patient.patient_id