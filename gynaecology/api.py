"""
Gynaecology API endpoints.
"""

from django.shortcuts import get_object_or_404

from ninja import Router

from .models import GynecologyConsultation
from patients.models import Patient

from .schemas import (
    GynecologyConsultationCreateSchema,
    GynecologyConsultationResponseSchema,
    GynecologyConsultationListSchema,
)

router = Router()


@router.post(
    "/",
    response=GynecologyConsultationResponseSchema,
)
def create_consultation(
    request,
    payload: GynecologyConsultationCreateSchema,
):
    """
    Create a gynaecology consultation.
    """

    # Retrieve the patient.
    patient = get_object_or_404(
        Patient,
        id=payload.patient_id,
    )

    # Create the consultation.
    consultation = GynecologyConsultation.objects.create(
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

    return consultation


@router.get(
    "/",
    response=list[GynecologyConsultationListSchema],
)
def list_consultations(request):
    """
    Retrieve all gynaecology consultations.
    """

    return GynecologyConsultation.objects.select_related(
        "patient"
    ).all()