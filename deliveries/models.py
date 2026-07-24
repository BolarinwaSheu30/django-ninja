"""
Delivery model.
"""

from django.db import models

from pregnancies.models import Pregnancy


class DeliveryMode(models.TextChoices):
    """
    Allowed delivery methods.
    """

    VAGINAL = "Vaginal", "Vaginal"
    CAESAREAN = "Caesarean", "Caesarean"
    ASSISTED = "Assisted", "Assisted"


class BabyStatus(models.TextChoices):
    """
    Baby outcome at delivery.
    """

    ALIVE = "Alive", "Alive"
    STILLBIRTH = "Stillbirth", "Stillbirth"


class BabySex(models.TextChoices):
    """
    Baby sex.
    """

    MALE = "Male", "Male"
    FEMALE = "Female", "Female"


class Delivery(models.Model):
    """
    Stores delivery information.
    """

    pregnancy = models.OneToOneField(
        Pregnancy,
        on_delete=models.CASCADE,
        related_name="delivery",
    )

    delivery_datetime = models.DateTimeField(
        db_index=True,
    )

    mode_of_delivery = models.CharField(
        max_length=20,
        choices=DeliveryMode.choices,
    )

    baby_sex = models.CharField(
        max_length=10,
        choices=BabySex.choices,
    )

    birth_weight_kg = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    apgar_1_min = models.PositiveIntegerField()

    apgar_5_min = models.PositiveIntegerField()

    baby_status = models.CharField(
        max_length=20,
        choices=BabyStatus.choices,
        default=BabyStatus.ALIVE,
        db_index=True,
    )

    estimated_blood_loss_ml = models.PositiveIntegerField()

    maternal_complications = models.TextField(
        blank=True,
        default="",
    )

    notes = models.TextField(
        blank=True,
        default="",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = [
            "-delivery_datetime",
        ]

        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"

        indexes = [
            models.Index(
                fields=[
                    "delivery_datetime",
                    "baby_status",
                ],
            ),
        ]

    @property
    def patient(self):
        """
        Return the patient associated
        with this delivery.
        """

        return self.pregnancy.patient

    def __str__(self) -> str:
        """
        Return a readable
        representation.
        """

        return (
            f"{self.patient.patient_id}"
            f" - {self.delivery_datetime.date()}"
        )