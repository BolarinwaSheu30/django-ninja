"""
Central API configuration.
"""

from ninja import NinjaAPI

from antenatal.api import router as antenatal_router

from patients.api import router as patients_router

from pregnancies.api import router as pregnancies_router

# Main API instance
api = NinjaAPI(
    title="Maternal Care Management System",
    version="1.0.0"
)

# Register patient routes
api.add_router(
    "/patients/",
    patients_router
)
api.add_router(
    "/pregnancies/",
    pregnancies_router,
)
api.add_router(
    '/antenatal/',
    antenatal_router,
)