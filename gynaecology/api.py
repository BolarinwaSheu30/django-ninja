"""
Gynaecology API endpoints.
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

from patients.models import Patient

from .models import GynecologyConsultation
from .schemas import (
    GynecologyConsultationCreateSchema,
)

router = Router()


def _consultation_to_dict(
    consultation: GynecologyConsultation,
) -> dict:
    """
    Convert a consultation into a
    detailed dictionary.
    """

    return {
        "id": consultation.id,
        "patient_id": consultation.patient.patient_id,
        "consultation_date": consultation.consultation_date,
        "consultation_type": consultation.consultation_type,
        "presenting_complaint": consultation.presenting_complaint,
        "history": consultation.history,
        "examination_findings": consultation.examination_findings,
        "diagnosis": consultation.diagnosis,
        "treatment": consultation.treatment,
        "follow_up_plan": consultation.follow_up_plan,
        "notes": consultation.notes,
    }


def _consultation_list_to_dict(
    consultation: GynecologyConsultation,
) -> dict:
    """
    Convert a consultation into a
    lightweight dictionary.
    """

    return {
        "id": consultation.id,
        "patient_id": consultation.patient.patient_id,
        "consultation_date": consultation.consultation_date,
        "consultation_type": consultation.consultation_type,
        "diagnosis": consultation.diagnosis,
    }


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
        404: ErrorResponseSchema,
    },
)
def create_consultation(
    request,
    payload: GynecologyConsultationCreateSchema,
):
    """
    Create a gynaecology consultation.
    """

    patient = _get_patient(
        payload.patient_id,
    )

    if not patient:
        return error_response(
            "Patient not found",
            404,
        )

    consultation = (
        GynecologyConsultation.objects.create(
            patient=patient,
            consultation_date=payload.consultation_date,
            consultation_type=payload.consultation_type,
            presenting_complaint=payload.presenting_complaint,
            history=payload.history,
            examination_findings=payload.examination_findings,
            diagnosis=payload.diagnosis,
            treatment=payload.treatment,
            follow_up_plan=payload.follow_up_plan,
            notes=payload.notes,
        )
    )

    return success_response(
        "Consultation created successfully",
        _consultation_to_dict(
            consultation,
        ),
    )


@router.get(
    "/",
    response=SuccessResponseSchema,
)
def list_consultations(
    request,
):
    """
    Retrieve all consultations.
    """

    consultations = (
        GynecologyConsultation.objects
        .select_related("patient")
        .order_by("-consultation_date")
    )

    return success_response(
        "Consultations retrieved successfully",
        [
            _consultation_list_to_dict(
                consultation,
            )
            for consultation in consultations
        ],
    )