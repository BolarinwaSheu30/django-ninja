from django.contrib import admin

from .models import Delivery


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        "pregnancy",
        "delivery_datetime",
        "mode_of_delivery",
        "baby_sex",
        "birth_weight_kg",
        "baby_status",
    )

    list_filter = (
        "mode_of_delivery",
        "baby_status",
    )

    ordering = (
        "-delivery_datetime",
    )