"""
Pregnancy API endpoints.
"""

# Import Django's shortcut for retrieving
# an object or returning a 404 error.
from typing import Optional
from datetime import timedelta
from django.shortcuts import get_object_or_404

# Import Django Ninja's Router.
from ninja import Router

# Import our models.
from .models import Pregnancy, PregnancyStatus
from patients.models import Patient

# Import our schemas.
from .schemas import (
    PregnancyCreateSchema,
    PregnancyResponseSchema,
    PregnancyListSchema,
    ErrorSchema
)

# Create a router for pregnancy endpoints.
router = Router()


@router.post(
    "/",
    response={
        200: PregnancyResponseSchema,
        400: ErrorSchema,
    },
)
def create_pregnancy(
    request,
    payload: PregnancyCreateSchema,
):
    """
    Register a new pregnancy.
    """

    # Find the patient using the ID
    # supplied in the request.
    patient = get_object_or_404(
        Patient,
        id=payload.patient_id,
    )
    # Check whether the patient already has
    # an ongoing pregnancy.
    existing_pregnancy = Pregnancy.objects.filter(
        patient=patient,
        pregnancy_status=PregnancyStatus.ONGOING,
    ).exists()
    # Prevent creating another ongoing pregnancy.
    if existing_pregnancy:
        return 400, {
            "detail": (
                "This patient already has "
                "an ongoing pregnancy."
            )
    }
    edd = payload.lmp + timedelta(days=280)
    days_pregnant = (
        payload.booking_date - payload.lmp
    ).days

    gestational_age_weeks = (
        days_pregnant // 7
    )

    # Create the pregnancy.
    pregnancy = Pregnancy.objects.create(
        patient=patient,
        booking_date=payload.booking_date,
        lmp=payload.lmp,

    # Use the values calculated by the backend.
        edd=edd,
        gestational_age_weeks=gestational_age_weeks,

        gravida=payload.gravida,
        parity=payload.parity,
        # Every new pregnancy starts as ongoing
        pregnancy_status= PregnancyStatus.ONGOING,
        notes=payload.notes,
    )
    # Return the newly created pregnancy.
    return pregnancy

@router.get(
    "/",
    response=list[PregnancyListSchema],
)
def list_pregnancies(
    request,
    status:Optional[str] = None,
    ):
    """
    Retrieve pregnancies with optional
    status filtering.
    """
    pregnancies = Pregnancy.objects.select_related(
        "patient"
    ).all()

    if status:
        pregnancies = pregnancies.filter(
            pregnancy_status__iexact=status
        )
    return pregnancies