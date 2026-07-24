"""
Postnatal Care API endpoints.
"""

from ninja import Router

from config.common_schemas import (
    SuccessResponseSchema,
    ErrorResponseSchema,
)
from config.utils import (
    success_response,
    error_response,
)

from deliveries.models import Delivery

from .models import PostnatalVisit
from .schemas import (
    PostnatalVisitCreateSchema,
)

router = Router()


def _postnatal_to_dict(
    visit: PostnatalVisit,
) -> dict:
    """
    Convert a PostnatalVisit model instance
    into a detailed dictionary.
    """

    return {
        "id": visit.id,
        "delivery_id": visit.delivery.id,
        "patient_id": visit.delivery.pregnancy.patient.patient_id,
        "visit_number": visit.visit_number,
        "visit_date": visit.visit_date,
        "blood_pressure": visit.blood_pressure,
        "temperature_c": visit.temperature_c,
        "pulse_rate": visit.pulse_rate,
        "lochia": visit.lochia,
        "breastfeeding_status": visit.breastfeeding_status,
        "wound_healing": visit.wound_healing,
        "baby_weight_kg": visit.baby_weight_kg,
        "feeding_well": visit.feeding_well,
        "immunization_given": visit.immunization_given,
        "family_planning_counseled": visit.family_planning_counseled,
        "next_appointment_date": visit.next_appointment_date,
        "notes": visit.notes,
    }


def _postnatal_list_to_dict(
    visit: PostnatalVisit,
) -> dict:
    """
    Convert a PostnatalVisit model instance
    into a lightweight dictionary.
    """

    return {
        "id": visit.id,
        "patient_id": visit.delivery.pregnancy.patient.patient_id,
        "visit_number": visit.visit_number,
        "visit_date": visit.visit_date,
        "baby_weight_kg": visit.baby_weight_kg,
        "feeding_well": visit.feeding_well,
    }


def _get_delivery(
    delivery_id: int,
) -> Delivery | None:
    """
    Retrieve a delivery by ID.
    """

    return Delivery.objects.filter(
        id=delivery_id,
    ).first()


@router.post(
    "/",
    response={
        200: SuccessResponseSchema,
        400: ErrorResponseSchema,
        404: ErrorResponseSchema,
    },
)
def create_postnatal_visit(
    request,
    payload: PostnatalVisitCreateSchema,
):
    """
    Create a postnatal visit.
    """

    delivery = _get_delivery(
        payload.delivery_id,
    )

    if not delivery:
        return error_response(
            "Delivery not found.",
            404,
        )

    visit_number = (
        PostnatalVisit.objects.filter(
            delivery=delivery,
        ).count() + 1
    )

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
        family_planning_counseled=payload.family_planning_counseled,
        next_appointment_date=payload.next_appointment_date,
        notes=payload.notes,
    )

    return success_response(
        "Postnatal visit recorded successfully.",
        _postnatal_to_dict(
            visit,
        ),
    )


@router.get(
    "/",
    response=SuccessResponseSchema,
)
def list_postnatal_visits(
    request,
):
    """
    Retrieve all postnatal visits.
    """

    visits = (
        PostnatalVisit.objects
        .select_related(
            "delivery__pregnancy__patient",
        )
        .order_by("-visit_date")
    )

    return success_response(
        "Postnatal visits retrieved successfully.",
        [
            _postnatal_list_to_dict(
                visit,
            )
            for visit in visits
        ],
    )