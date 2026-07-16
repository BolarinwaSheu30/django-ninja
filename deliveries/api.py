"""
Delivery API endpoints.
"""

from django.shortcuts import get_object_or_404

from ninja import Router

from .models import Delivery

from users.auth import JWTAuth

from users.permissions import require_roles

from users.models import UserRole

from pregnancies.models import (
    Pregnancy,
    PregnancyStatus,
)

from .schemas import (
    DeliveryCreateSchema,
    DeliveryResponseSchema,
    DeliveryListSchema,
)

auth = JWTAuth()
router = Router()


@router.post(
    "/",
    response=DeliveryResponseSchema,
    auth = auth,
)
def create_delivery(
    request,
    payload: DeliveryCreateSchema,
):
    """
    Record a delivery.
    """



    # Only Doctors and Admins can create deliveries.
    require_roles(
        request.auth,
        [
            UserRole.DOCTOR,
            UserRole.ADMIN,
        ],
    )

    # Retrieve the pregnancy.
    pregnancy = get_object_or_404(
        Pregnancy,
        id=payload.pregnancy_id,
    )

    # Create the delivery record.
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

    # Automatically mark the pregnancy
    # as delivered.
    pregnancy.pregnancy_status = (
        PregnancyStatus.DELIVERED
    )
    pregnancy.save()

    return delivery


@router.get(
    "/",
    response=list[DeliveryListSchema],
)
def list_deliveries(request):
    """
    Retrieve all deliveries.
    """

    return Delivery.objects.select_related(
        "pregnancy__patient"
    ).all()