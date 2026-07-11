"""
Antenatal Care API endpoints.
"""

# Import Django shortcut.
from django.shortcuts import get_object_or_404

# Import Django Ninja Router.
from ninja import Router

# Import models.
from .models import AntenatalVisit
from pregnancies.models import Pregnancy

# Import schemas.
from .schemas import (
    AntenatalVisitCreateSchema,
    AntenatalVisitResponseSchema,
    AntenatalVisitListSchema,
)

# Create router.
router = Router()


@router.post(
    "/",
    response=AntenatalVisitResponseSchema,
)
def create_antenatal_visit(
    request,
    payload: AntenatalVisitCreateSchema,
):
    """
    Create an antenatal visit.
    """

    # Retrieve the pregnancy.
    pregnancy = get_object_or_404(
        Pregnancy,
        id=payload.pregnancy_id,
    )

    # Determine the next visit number.
    visit_number = (
        AntenatalVisit.objects.filter(
            pregnancy=pregnancy
        ).count() + 1
    )

    # Create the visit.
    visit = AntenatalVisit.objects.create(
        pregnancy=pregnancy,
        visit_date=payload.visit_date,
        visit_number=visit_number,
        weight_kg=payload.weight_kg,
        blood_pressure=payload.blood_pressure,
        fetal_heart_rate=payload.fetal_heart_rate,

        # Additional clinical observations.
        temperature_c=payload.temperature_c,
        pulse_rate=payload.pulse_rate,
        fundal_height_cm=payload.fundal_height_cm,
        fetal_movement_present=payload.fetal_movement_present,
        urine_protein=payload.urine_protein,
        urine_glucose=payload.urine_glucose,
        next_appointment_date=payload.next_appointment_date,

        notes=payload.notes,
)

    return visit


@router.get(
    "/",
    response=list[AntenatalVisitListSchema],
)
def list_antenatal_visits(request):
    """
    Retrieve all antenatal visits.
    """

    return AntenatalVisit.objects.select_related(
        "pregnancy__patient"
    ).all()