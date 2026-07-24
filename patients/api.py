"""
Patient API endpoints.
"""

from django.db.models import Q
from ninja import Router
from typing import Optional

from .models import Patient
from .schemas import (   
    PatientCreateSchema,
    PatientUpdateSchema,
    PaginatedPatientsResponseSchema,
)
from config.utils import (
    success_response,
    error_response,
)
from config.common_schemas import (
    SuccessResponseSchema,
    ErrorResponseSchema,
)

# Create router for patient endpoints
router = Router()

def _patient_to_dict(patient):
    """
    Convert a Patient model instance
    into a JSON-friendly dictionary.
    """

    return {
        "id": patient.id,
        "patient_id": patient.patient_id,
        "first_name": patient.first_name,
        "last_name": patient.last_name,
        "date_of_birth": patient.date_of_birth,
        "gender": patient.gender,
        "blood_group": patient.blood_group,
        "marital_status": patient.marital_status,
        "occupation": patient.occupation,
        "phone_number": patient.phone_number,
        "address": patient.address,
        "next_of_kin_name": patient.next_of_kin_name,
        "next_of_kin_phone": patient.next_of_kin_phone,
        "emergency_contact": patient.emergency_contact,
    }


@router.get(
    "/health",
    response=SuccessResponseSchema,
        )

def health_check(request):
    """
    Verify API is working.
    """

    return success_response(
        "Maternal Care API is running"
    )


@router.post(
    "/",
    response={
        200: SuccessResponseSchema,
        400:ErrorResponseSchema,
    }
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

        gender=payload.gender,
        blood_group=payload.blood_group,
        marital_status=payload.marital_status,
        occupation=payload.occupation,
        next_of_kin_name=payload.next_of_kin_name,
        next_of_kin_phone=payload.next_of_kin_phone,

        phone_number=payload.phone_number,
        address=payload.address,
        emergency_contact=payload.emergency_contact,
    )

    return success_response(
        "Patient created successfully",
        _patient_to_dict(patient),
    )

    


@router.get(
    "/",
    response=PaginatedPatientsResponseSchema,
)
def list_patients(
    request,
    search: Optional[str] = None,
    page: int = 1,
    page_size: int = 10,
):
    """
    Retrieve patients with optional search
    and pagination.
    """

    patients = Patient.objects.order_by("-id")

    # Search filtering.
    if search:
        patients = patients.filter(
            Q(patient_id__icontains=search) |
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search)
        )

    # Total records before slicing.
    total_count = patients.count()

    # Pagination calculation.
    start = (page - 1) * page_size
    end = start + page_size

    paginated_patients = patients[start:end]

    return success_response(
         "Patients retrieved successfully",
         {
              "count": total_count,
              "page": page,
              "page_size": page_size,
              "results": [
                   {
                        "id": patient.id,
                        "patient_id": patient.patient_id,
                        "first_name": patient.first_name,
                        "last_name": patient.last_name,
                        "gender": patient.gender,
                        "phone_number": patient.phone_number,
                   }
                   for patient in paginated_patients
              ],

         },
    )
            
            
        
    


@router.get(
    "/{patient_id}",
    response={
        200: SuccessResponseSchema,
        404: ErrorResponseSchema,
    },
)
def get_patient(
    request,
    patient_id: int
):
    """
    Retrieve a single patient by ID.
    """

    patient = Patient.objects.filter(id=patient_id).first()

    if not patient:
        return error_response(
            "Patient not found",
            404,
        )

    return success_response(
        "Patient retrieved successfully",
        _patient_to_dict(patient),
    )
    


@router.put(
    "/{patient_id}",
    response={
        200: SuccessResponseSchema,
        404: ErrorResponseSchema,
    }
)
def update_patient(
    request,
    patient_id: int,
    payload: PatientUpdateSchema
):
    """
    Update an existing patient.
    """

    patient = Patient.objects.filter(id=patient_id).first()

    if not patient:
        return error_response(
            "Patient not found",
            404,
        )

    patient.first_name =payload.first_name
    patient.last_name =payload.last_name
    patient.date_of_birth =payload.date_of_birth
    patient.phone_number =payload.phone_number
    patient.address =payload.address
    patient.emergency_contact =payload.emergency_contact
    patient.gender =payload.gender
    patient.blood_group =payload.blood_group
    patient.marital_status =payload.marital_status
    patient.occupation =payload.occupation
    patient.next_of_kin_name =payload.next_of_kin_name
    patient.next_of_kin_phone =payload.next_of_kin_phone

    patient.save()

    return success_response(
        "Patient updated successfully",
        _patient_to_dict(patient),
    )


@router.delete(
    "/{patient_id}",
    response = {
        200: SuccessResponseSchema,
        404: ErrorResponseSchema,
    },
    )
def delete_patient(
    request,
    patient_id: int
):
    """
    Delete a patient record.
    """

    patient = Patient.objects.filter(id=patient_id).first()

    if not patient:
        return error_response(
            "Patient not found",
            404,
        )

    patient.delete()

    return success_response(
        "Patient deleted successfully"
    )