from django.contrib import admin

from .models import AntenatalVisit


@admin.register(AntenatalVisit)
class AntenatalVisitAdmin(admin.ModelAdmin):
    list_display = (
        "pregnancy",
        "visit_number",
        "visit_date",
        "blood_pressure",
        "fetal_heart_rate",
    )

    list_filter = (
        "visit_date",
    )

    ordering = (
        "-visit_date",
    )