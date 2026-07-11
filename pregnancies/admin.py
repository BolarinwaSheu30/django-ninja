"""
Admin configuration for the Pregnancy model.
"""

# Import Django admin.
from django.contrib import admin

# Import our models.
from .models import Pregnancy


@admin.register(Pregnancy)
class PregnancyAdmin(admin.ModelAdmin):
    """
    Customize how pregnancies appear
    in the Django admin.
    """

    # Columns displayed in the list view.
    list_display = (
        "patient",
        "booking_date",
        "edd",
        "gestational_age_weeks",
        "pregnancy_status",
    )

    # Allow searching by patient ID or name.
    search_fields = (
        "patient__patient_id",
        "patient__first_name",
        "patient__last_name",
    )

    # Filter pregnancies by status.
    list_filter = (
        "pregnancy_status",
    )

    # Order newest pregnancies first.
    ordering = (
        "-booking_date",
    )