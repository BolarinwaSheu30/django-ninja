from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """
    Configure Patient display
    inside Django admin.
    """

    list_display = (
        "patient_id",
        "first_name",
        "last_name",
        "phone_number",
        "created_at",
    )

    search_fields = (
        "patient_id",
        "first_name",
        "last_name",
    )