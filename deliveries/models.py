from django.db import models

# Import Pregnancy model.
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


class Delivery(models.Model):
    """
    Stores delivery information.
    """

    # One delivery belongs to one pregnancy.
    pregnancy = models.OneToOneField(
        Pregnancy,
        on_delete=models.CASCADE,
        related_name="delivery",
    )

    # Date and time of delivery.
    delivery_datetime = models.DateTimeField()

    # Mode of delivery.
    mode_of_delivery = models.CharField(
        max_length=20,
        choices=DeliveryMode.choices,
    )

    # Baby sex.
    baby_sex = models.CharField(
        max_length=10,
    )

    # Birth weight in kilograms.
    birth_weight_kg = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    # Apgar score at 1 minute.
    apgar_1_min = models.PositiveIntegerField()

    # Apgar score at 5 minutes.
    apgar_5_min = models.PositiveIntegerField()

    # Baby status.
    baby_status = models.CharField(
        max_length=20,
        choices=BabyStatus.choices,
        default=BabyStatus.ALIVE,
    )

    # Estimated blood loss in mL.
    estimated_blood_loss_ml = models.PositiveIntegerField()

    # Maternal complications.
    maternal_complications = models.TextField(
        blank=True,
        default="",
    )

    # Additional notes.
    notes = models.TextField(
        blank=True,
        default="",
    )

    # Record creation timestamp.
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        """
        Display delivery information.
        """

        return (
            f"{self.pregnancy.patient.patient_id} - "
            f"{self.delivery_datetime.date()}"
        )