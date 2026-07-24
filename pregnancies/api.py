"""
Pregnancy API endpoints.
"""

from datetime import date, timedelta
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

from patients.models import Patient

from .models import Pregnancy, PregnancyStatus
from .schemas import PregnancyCreateSchema


router = Router()


def _pregnancy_to_dict(
    pregnancy: Pregnancy,
) -> dict:
    """
    Convert a Pregnancy model instance
    into a detailed dictionary.
    """

    return {
        "id": pregnancy.id,
        "patient_id": pregnancy.patient.patient_id,
        "booking_date": pregnancy.booking_date,
        "lmp": pregnancy.lmp,
        "edd": pregnancy.edd,
        "gestational_age_weeks": pregnancy.gestational_age_weeks,
        "gravida": pregnancy.gravida,
        "parity": pregnancy.parity,
        "pregnancy_status": pregnancy.pregnancy_status,
        "notes": pregnancy.notes,
    }


def _pregnancy_list_to_dict(
    pregnancy: Pregnancy,
) -> dict:
    """
    Convert a Pregnancy model instance
    into a lightweight dictionary.
    """

    return {
        "id": pregnancy.id,
        "patient_id": pregnancy.patient.patient_id,
        "booking_date": pregnancy.booking_date,
        "edd": pregnancy.edd,
        "gestational_age_weeks": pregnancy.gestational_age_weeks,
        "pregnancy_status": pregnancy.pregnancy_status,
    }


def _calculate_pregnancy_dates(
    booking_date: date,
    lmp: date,
) -> tuple[date, int]:
    """
    Calculate EDD and gestational age.
    """

    edd = lmp + timedelta(days=280)

    gestational_age_weeks = (
        booking_date - lmp
    ).days // 7

    return edd, gestational_age_weeks


def _get_patient(
    patient_id: int,
):
    """
    Retrieve a patient by ID.
    """

    return Patient.objects.filter(
        id=patient_id,
    ).first()


@router.post(
    "/",
    response={
        200: SuccessResponseSchema,
        400: ErrorResponseSchema,
        404: ErrorResponseSchema,
    },
)
def create_pregnancy(
    request,
    payload: PregnancyCreateSchema,
):
    """
    Register a new pregnancy.
    """

    patient = _get_patient(
        payload.patient_id,
    )

    if not patient:
        return error_response(
            "Patient not found",
            404,
        )

    if Pregnancy.objects.filter(
        patient=patient,
        pregnancy_status=PregnancyStatus.ONGOING,
    ).exists():
        return error_response(
            "This patient already has an ongoing pregnancy.",
            400,
        )

    if payload.booking_date < payload.lmp:
        return error_response(
            "Booking date cannot be earlier than LMP.",
            400,
        )

    edd, gestational_age_weeks = _calculate_pregnancy_dates(
        payload.booking_date,
        payload.lmp,
    )

    pregnancy = Pregnancy.objects.create(
        patient=patient,
        booking_date=payload.booking_date,
        lmp=payload.lmp,
        edd=edd,
        gestational_age_weeks=gestational_age_weeks,
        gravida=payload.gravida,
        parity=payload.parity,
        pregnancy_status=PregnancyStatus.ONGOING,
        notes=payload.notes,
    )

    return success_response(
        "Pregnancy registered successfully",
        _pregnancy_to_dict(
            pregnancy,
        ),
    )


@router.get(
    "/",
    response=SuccessResponseSchema,
)
def list_pregnancies(
    request,
    status: Optional[str] = None,
):
    """
    Retrieve pregnancies with optional
    status filtering.
    """

    pregnancies = Pregnancy.objects.select_related(
        "patient",
    ).order_by("-id")

    if status:
        pregnancies = pregnancies.filter(
            pregnancy_status__iexact=status,
        )

    return success_response(
        "Pregnancies retrieved successfully",
        [
            _pregnancy_list_to_dict(
                pregnancy,
            )
            for pregnancy in pregnancies
        ],
    )