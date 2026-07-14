from django.contrib import admin

from .models import GynecologyConsultation


@admin.register(GynecologyConsultation)
class GynecologyConsultationAdmin(admin.ModelAdmin):
    list_display = (
        "patient",
        "consultation_date",
        "consultation_type",
    )

    list_filter = (
        "consultation_type",
    )

    ordering = (
        "-consultation_date",
    )