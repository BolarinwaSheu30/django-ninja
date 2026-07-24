"""
Schemas for the Dashboard API.
"""

from ninja import Schema


class DashboardDataSchema(Schema):
    """
    Dashboard summary statistics.
    """

    total_patients: int

    ongoing_pregnancies: int

    delivered_pregnancies: int

    total_antenatal_visits: int

    total_deliveries: int

    total_postnatal_visits: int

    total_gynaecology_consultations: int


class DashboardResponseSchema(Schema):
    """
    Standard response returned by
    the dashboard summary endpoint.
    """

    status: str

    message: str

    data: DashboardDataSchema