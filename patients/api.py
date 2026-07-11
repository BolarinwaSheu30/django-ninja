"""
Patient API endpoints.
"""

from django.shortcuts import get_object_or_404

from ninja import Router

from .models import Patient
from .schemas import (
    PatientCreateSchema,
    PatientUpdateSchema,
    PatientResponseSchema,
    PatientListSchema,
)

# Create router for patient endpoints
router = Router()


@router.get("/health")
def health_check(request):
    """
    Verify API is working.
    """

    return {
        "status": "success",
        "message": "Maternal Care API is running"
    }


@router.post(
    "/",
    response=PatientResponseSchema
)
def create_patient(
    request,
    payload: PatientCreateSchema
):
    """
    Create a patient record.
    """

    patient = Patient.objects.create(
        first_name=payload.first_name,
        last_name=payload.last_name,
        date_of_birth=payload.date_of_birth,

        gender = payload.gender,
        blood_group = payload.blood_group,
        marital_status = payload.marital_status,
        occupation = payload.occupation,
        next_of_kin_name = payload.next_of_kin_name,
        next_of_kin_phone = payload.next_of_kin_phone,

        phone_number=payload.phone_number,
        address=payload.address,
        emergency_contact=payload.emergency_contact,
    )

    return patient


@router.get(
    "/",
    response=list[PatientListSchema]
)
def list_patients(request):
    """
    Retrieve all patients.

    Returns a simplified patient list.
    """

    return Patient.objects.all()

@router.get(
    "/{patient_id}",
    response=PatientResponseSchema
)
def get_patient(
    request,
    patient_id: int
):
    """
    Retrieve a single patient by ID.
    """

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )

    return patient

@router.put(
    "/{patient_id}",
    response=PatientResponseSchema
)
def update_patient(
    request,
    patient_id: int,
    payload: PatientUpdateSchema
):
    """
    Update an existing patient.
    """

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )

    patient.first_name = payload.first_name
    patient.last_name = payload.last_name
    patient.date_of_birth = payload.date_of_birth
    patient.phone_number = payload.phone_number
    patient.address = payload.address
    patient.emergency_contact = payload.emergency_contact
    patient.gender = payload.gender
    patient.blood_group = payload.blood_group
    patient.marital_status = payload.marital_status
    patient.occupation = payload.occupation
    patient.next_of_kin_name = payload.next_of_kin_name
    patient.next_of_kin_phone = payload.next_of_kin_phone

    patient.save()

    return patient


@router.delete("/{patient_id}")
def delete_patient(
    request,
    patient_id: int
):
    """
    Delete a patient record.
    """

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )

    patient.delete()

    return {
        "message": "Patient deleted successfully"
    }