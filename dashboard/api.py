"""
Dashboard API endpoints.
"""

from ninja import Router

from config.common_schemas import SuccessResponseSchema
from config.utils import success_response

from antenatal.models import AntenatalVisit
from deliveries.models import Delivery
from gynaecology.models import GynecologyConsultation
from patients.models import Patient
from postnatal.models import PostnatalVisit
from pregnancies.models import Pregnancy, PregnancyStatus

router = Router()


def _dashboard_summary():
    """
    Build dashboard statistics.
    """

    return {
        "total_patients": Patient.objects.count(),
        "ongoing_pregnancies": Pregnancy.objects.filter(
            pregnancy_status=PregnancyStatus.ONGOING,
        ).count(),
        "delivered_pregnancies": Pregnancy.objects.filter(
            pregnancy_status=PregnancyStatus.DELIVERED,
        ).count(),
        "total_antenatal_visits": AntenatalVisit.objects.count(),
        "total_deliveries": Delivery.objects.count(),
        "total_postnatal_visits": PostnatalVisit.objects.count(),
        "total_gynaecology_consultations":
            GynecologyConsultation.objects.count(),
    }


@router.get(
    "/summary",
    response=SuccessResponseSchema,
)
def dashboard_summary(request):
    """
    Return dashboard summary statistics.
    """

    return success_response(
        "Dashboard summary retrieved successfully",
        _dashboard_summary(),
    )