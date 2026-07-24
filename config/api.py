"""
Central API configuration.
"""

from ninja import NinjaAPI

from antenatal.api import router as antenatal_router
from dashboard.api import router as dashboard_router
from deliveries.api import router as deliveries_router
from gynaecology.api import router as gynaecology_router
from patients.api import router as patients_router
from postnatal.api import router as postnatal_router
from pregnancies.api import router as pregnancies_router
from users.api import router as users_router


api = NinjaAPI(
    title="Maternal Care Management System",
    version="1.0.0",
)

# Register API routers
api.add_router("/patients/", patients_router)
api.add_router("/pregnancies/", pregnancies_router)
api.add_router("/antenatal/", antenatal_router)
api.add_router("/deliveries/", deliveries_router)
api.add_router("/postnatal/", postnatal_router)
api.add_router("/gynaecology/", gynaecology_router)
api.add_router("/auth/", users_router)
api.add_router("/dashboard/", dashboard_router)