"""
Delivery API endpoints.
"""
from typing import Optional
from ninja import Router

from config.common_schemas import (
    SuccessResponseSchema,
    ErrorResponseSchema,
)
from config.utils import (
    success_response,
    error_response,
)

from users.auth import JWTAuth
from users.permissions import require_roles
from users.models import UserRole

from pregnancies.models import (
    Pregnancy,
    PregnancyStatus,
)

from .models import Delivery
from .schemas import DeliveryCreateSchema


auth = JWTAuth()
router = Router()


def _delivery_to_dict(
    delivery: Delivery,
) -> dict:
    """
    Convert a Delivery model instance
    into a detailed dictionary.
    """

    return {
        "id": delivery.id,
        "pregnancy_id": delivery.pregnancy.id,
        "patient_id": delivery.pregnancy.patient.patient_id,
        "delivery_datetime": delivery.delivery_datetime,
        "mode_of_delivery": delivery.mode_of_delivery,
        "baby_sex": delivery.baby_sex,
        "birth_weight_kg": delivery.birth_weight_kg,
        "apgar_1_min": delivery.apgar_1_min,
        "apgar_5_min": delivery.apgar_5_min,
        "baby_status": delivery.baby_status,
        "estimated_blood_loss_ml": delivery.estimated_blood_loss_ml,
        "maternal_complications": delivery.maternal_complications,
        "notes": delivery.notes,
    }


def _delivery_list_to_dict(
    delivery: Delivery,
) -> dict:
    """
    Convert a Delivery model instance
    into a lightweight dictionary.
    """

    return {
        "id": delivery.id,
        "patient_id": delivery.pregnancy.patient.patient_id,
        "delivery_datetime": delivery.delivery_datetime,
        "mode_of_delivery": delivery.mode_of_delivery,
        "baby_sex": delivery.baby_sex,
        "baby_status": delivery.baby_status,
    }


def _get_pregnancy(
    pregnancy_id: int,
) -> Optional[Pregnancy]:
    """
    Retrieve a pregnancy by ID.
    """

    return Pregnancy.objects.filter(
        id=pregnancy_id,
    ).first()


@router.post(
    "/",
    auth=auth,
    response={
        200: SuccessResponseSchema,
        400: ErrorResponseSchema,
        403: ErrorResponseSchema,
        404: ErrorResponseSchema,
    },
)
def create_delivery(
    request,
    payload: DeliveryCreateSchema,
):
    """
    Record a delivery.
    """

    require_roles(
        request.auth,
        [
            UserRole.DOCTOR,
            UserRole.ADMIN,
        ],
    )

    pregnancy = _get_pregnancy(
        payload.pregnancy_id,
    )

    if not pregnancy:
        return error_response(
            "Pregnancy not found",
            404,
        )

    if pregnancy.pregnancy_status == PregnancyStatus.DELIVERED:
        return error_response(
            "This pregnancy has already been delivered.",
            400,
        )

    delivery = Delivery.objects.create(
        pregnancy=pregnancy,
        delivery_datetime=payload.delivery_datetime,
        mode_of_delivery=payload.mode_of_delivery,
        baby_sex=payload.baby_sex,
        birth_weight_kg=payload.birth_weight_kg,
        apgar_1_min=payload.apgar_1_min,
        apgar_5_min=payload.apgar_5_min,
        baby_status=payload.baby_status,
        estimated_blood_loss_ml=payload.estimated_blood_loss_ml,
        maternal_complications=payload.maternal_complications,
        notes=payload.notes,
    )

    pregnancy.pregnancy_status = PregnancyStatus.DELIVERED
    pregnancy.save(
        update_fields=[
            "pregnancy_status",
        ]
    )

    return success_response(
        "Delivery recorded successfully",
        _delivery_to_dict(
            delivery,
        ),
    )


@router.get(
    "/",
    response=SuccessResponseSchema,
)
def list_deliveries(
    request,
):
    """
    Retrieve all deliveries.
    """

    deliveries = (
        Delivery.objects
        .select_related(
            "pregnancy__patient",
        )
        .order_by("-delivery_datetime")
    )

    return success_response(
        "Deliveries retrieved successfully",
        [
            _delivery_list_to_dict(
                delivery,
            )
            for delivery in deliveries
        ],
    )