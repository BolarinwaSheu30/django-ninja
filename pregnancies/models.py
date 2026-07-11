from django.db import models

# Import the Patient model.
# Every pregnancy belongs to one patient.
from patients.models import Patient


class PregnancyStatus(models.TextChoices):
    """
    Allowed pregnancy statuses.

    Using TextChoices ensures that
    only valid values are stored.
    """

    ONGOING = "Ongoing", "Ongoing"
    DELIVERED = "Delivered", "Delivered"
    MISCARRIAGE = "Miscarriage", "Miscarriage"
    STILLBIRTH = "Stillbirth", "Stillbirth"
    TERMINATED = "Terminated", "Terminated"


class Pregnancy(models.Model):
    """
    Represents a single pregnancy.

    One patient can have multiple pregnancies.
    """

    # Link this pregnancy to a patient.
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="pregnancies",
    )

    # Date the pregnancy was booked.
    booking_date = models.DateField()

    # Last Menstrual Period.
    lmp = models.DateField()

    # Estimated Date of Delivery.
    edd = models.DateField()

    # Gestational age in completed weeks
    # when the patient booked.
    gestational_age_weeks = models.PositiveIntegerField()

    # Number of pregnancies.
    gravida = models.PositiveIntegerField()

    # Number of deliveries after viability.
    parity = models.PositiveIntegerField()

    # Current pregnancy status.
    pregnancy_status = models.CharField(
        max_length=20,
        choices=PregnancyStatus.choices,
        default=PregnancyStatus.ONGOING,
    )

    # Additional clinical notes.
    notes = models.TextField(
        blank=True,
        default="",
    )

    # Date this record was created.
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        """
        Display the pregnancy in
        the Django admin.
        """

        return (
            f"{self.patient.patient_id} - "
            f"{self.booking_date}"
        )