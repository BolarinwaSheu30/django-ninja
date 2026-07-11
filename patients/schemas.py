"""
Schemas define the shape of data entering
and leaving our API.
"""

from datetime import date

from ninja import Schema


class PatientCreateSchema(Schema):
    """
    Schema used when creating a new patient.
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
    Schema returned when retrieving
    a patient record.
    """
    
    id: int
    patient_id:str

    first_name: str
    last_name: str
    date_of_birth: date


    gender:str
    blood_group:str
    marital_status: str
    occupation: str

    phone_number: str
    address: str

    next_of_kin_name:str
    next_of_kin_phone:str

    emergency_contact: str


class PatientListSchema(Schema):
    """
    Lightweight schema used when listing patients.
    """

    id: int
    patient_id: str
    first_name: str
    last_name: str
    gender: str
    phone_number: str

class PatientUpdateSchema(Schema):
    """
    Schema used when updating
    an existing patient.
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