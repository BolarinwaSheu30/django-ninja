from django.contrib import admin

from .models import PostnatalVisit


@admin.register(PostnatalVisit)
class PostnatalVisitAdmin(admin.ModelAdmin):
    list_display = (
        "delivery",
        "visit_number",
        "visit_date",
        "breastfeeding_status",
        "baby_weight_kg",
    )

    list_filter = (
        "breastfeeding_status",
        "immunization_given",
    )

    ordering = (
        "-visit_date",
    )