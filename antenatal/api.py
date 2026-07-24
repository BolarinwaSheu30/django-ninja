"""
Antenatal Care API endpoints.
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

from pregnancies.models import Pregnancy

from .models import AntenatalVisit
from .schemas import (
    AntenatalVisitCreateSchema,
)

router = Router()


def _antenatal_to_dict(
    visit: AntenatalVisit,
) -> dict:
    """
    Convert an antenatal visit
    into a detailed dictionary.
    """

    return {
        "id": visit.id,
        "pregnancy_id": visit.pregnancy.id,
        "patient_id": visit.pregnancy.patient.patient_id,
        "visit_number": visit.visit_number,
        "visit_date": visit.visit_date,
        "weight_kg": visit.weight_kg,
        "blood_pressure": visit.blood_pressure,
        "fetal_heart_rate": visit.fetal_heart_rate,
        "temperature_c": visit.temperature_c,
        "pulse_rate": visit.pulse_rate,
        "fundal_height_cm": visit.fundal_height_cm,
        "fetal_movement_present": visit.fetal_movement_present,
        "urine_protein": visit.urine_protein,
        "urine_glucose": visit.urine_glucose,
        "next_appointment_date": visit.next_appointment_date,
        "notes": visit.notes,
    }


def _antenatal_list_to_dict(
    visit: AntenatalVisit,
) -> dict:
    """
    Convert an antenatal visit
    into a lightweight dictionary.
    """

    return {
        "id": visit.id,
        "patient_id": visit.pregnancy.patient.patient_id,
        "visit_number": visit.visit_number,
        "visit_date": visit.visit_date,
        "blood_pressure": visit.blood_pressure,
        "weight_kg": visit.weight_kg,
    }


def _get_pregnancy(
    pregnancy_id: int,
):
    """
    Retrieve a pregnancy by ID.
    """

    return Pregnancy.objects.filter(
        id=pregnancy_id,
    ).first()


@router.post(
    "/",
    response={
        200: SuccessResponseSchema,
        400: ErrorResponseSchema,
        404: ErrorResponseSchema,
    },
)
def create_antenatal_visit(
    request,
    payload: AntenatalVisitCreateSchema,
):
    """
    Create an antenatal visit.
    """

    pregnancy = _get_pregnancy(
        payload.pregnancy_id,
    )

    if not pregnancy:
        return error_response(
            "Pregnancy not found",
            404,
        )

    visit_number = (
        AntenatalVisit.objects.filter(
            pregnancy=pregnancy,
        ).count()
        + 1
    )

    visit = AntenatalVisit.objects.create(
        pregnancy=pregnancy,
        visit_date=payload.visit_date,
        visit_number=visit_number,
        weight_kg=payload.weight_kg,
        blood_pressure=payload.blood_pressure,
        fetal_heart_rate=payload.fetal_heart_rate,
        temperature_c=payload.temperature_c,
        pulse_rate=payload.pulse_rate,
        fundal_height_cm=payload.fundal_height_cm,
        fetal_movement_present=payload.fetal_movement_present,
        urine_protein=payload.urine_protein,
        urine_glucose=payload.urine_glucose,
        next_appointment_date=payload.next_appointment_date,
        notes=payload.notes,
    )

    return success_response(
        "Antenatal visit created successfully",
        _antenatal_to_dict(
            visit,
        ),
    )


@router.get(
    "/",
    response=SuccessResponseSchema,
)
def list_antenatal_visits(
    request,
):
    """
    Retrieve all antenatal visits.
    """

    visits = (
        AntenatalVisit.objects
        .select_related(
            "pregnancy__patient",
        )
        .order_by("-visit_date")
    )

    return success_response(
        "Antenatal visits retrieved successfully",
        [
            _antenatal_list_to_dict(
                visit,
            )
            for visit in visits
        ],
    )