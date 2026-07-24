"""
Schemas define the shape of data entering
and leaving the Patients API.
"""

from datetime import date

from ninja import Schema


class PatientCreateSchema(Schema):
    """
    Schema used when creating
    a patient.
    """

    first_name: str
    last_name: str
    date_of_birth: date

    gender: str
    blood_group: str
    marital_status: str
    occupation: str

    next_of_kin_name: str
    next_of_kin_phone: str

    phone_number: str
    address: str
    emergency_contact: str


class PatientUpdateSchema(Schema):
    """
    Schema used when updating
    a patient.
    """

    first_name: str
    last_name: str
    date_of_birth: date

    gender: str
    blood_group: str
    marital_status: str
    occupation: str

    next_of_kin_name: str
    next_of_kin_phone: str

    phone_number: str
    address: str
    emergency_contact: str


class PatientResponseSchema(Schema):
    """
    Detailed patient information.
    """

    id: int
    patient_id: str

    first_name: str
    last_name: str
    date_of_birth: date

    gender: str
    blood_group: str
    marital_status: str
    occupation: str

    next_of_kin_name: str
    next_of_kin_phone: str

    phone_number: str
    address: str
    emergency_contact: str


class PatientListSchema(Schema):
    """
    Lightweight patient information
    for list endpoints.
    """

    id: int
    patient_id: str
    first_name: str
    last_name: str
    gender: str
    phone_number: str


class PaginatedPatientsDataSchema(Schema):
    """
    Paginated patient data.
    """

    count: int
    page: int
    page_size: int
    results: list[PatientListSchema]


class PaginatedPatientsResponseSchema(Schema):
    """
    Standard paginated response.
    """

    status: str
    message: str
    data: PaginatedPatientsDataSchema