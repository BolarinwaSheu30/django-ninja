"""
Postnatal Care API endpoints.
"""

from django.shortcuts import get_object_or_404

from ninja import Router

from .models import PostnatalVisit
from deliveries.models import Delivery

from .schemas import (
    PostnatalVisitCreateSchema,
    PostnatalVisitResponseSchema,
    PostnatalVisitListSchema,
)

router = Router()


@router.post(
    "/",
    response=PostnatalVisitResponseSchema,
)
def create_postnatal_visit(
    request,
    payload: PostnatalVisitCreateSchema,
):
    """
    Create a postnatal visit.
    """

    # Retrieve the delivery.
    delivery = get_object_or_404(
        Delivery,
        id=payload.delivery_id,
    )

    # Determine the next visit number.
    visit_number = (
        PostnatalVisit.objects.filter(
            delivery=delivery
        ).count() + 1
    )

    # Create the visit.
    visit = PostnatalVisit.objects.create(
        delivery=delivery,
        visit_date=payload.visit_date,
        visit_number=visit_number,
        blood_pressure=payload.blood_pressure,
        temperature_c=payload.temperature_c,
        pulse_rate=payload.pulse_rate,
        lochia=payload.lochia,
        breastfeeding_status=payload.breastfeeding_status,
        wound_healing=payload.wound_healing,
        baby_weight_kg=payload.baby_weight_kg,
        feeding_well=payload.feeding_well,
        immunization_given=payload.immunization_given,
        family_planning_counseled=(
            payload.family_planning_counseled
        ),
        next_appointment_date=(
            payload.next_appointment_date
        ),
        notes=payload.notes,
    )

    return visit


@router.get(
    "/",
    response=list[PostnatalVisitListSchema],
)
def list_postnatal_visits(request):
    """
    Retrieve all postnatal visits.
    """

    return PostnatalVisit.objects.select_related(
        "delivery__pregnancy__patient"
    ).all()