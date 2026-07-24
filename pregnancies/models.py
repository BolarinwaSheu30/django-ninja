"""
Pregnancy model.
"""

from django.db import models

from patients.models import Patient


class PregnancyStatus(models.TextChoices):
    """
    Allowed pregnancy statuses.
    """

    ONGOING = "Ongoing", "Ongoing"
    DELIVERED = "Delivered", "Delivered"
    MISCARRIAGE = "Miscarriage", "Miscarriage"
    STILLBIRTH = "Stillbirth", "Stillbirth"
    TERMINATED = "Terminated", "Terminated"


class Pregnancy(models.Model):
    """
    Represents a pregnancy belonging
    to a patient.
    """

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="pregnancies",
    )

    booking_date = models.DateField()

    lmp = models.DateField()

    edd = models.DateField(
        db_index=True,
    )

    gestational_age_weeks = models.PositiveIntegerField()

    gravida = models.PositiveIntegerField()

    parity = models.PositiveIntegerField()

    pregnancy_status = models.CharField(
        max_length=20,
        choices=PregnancyStatus.choices,
        default=PregnancyStatus.ONGOING,
        db_index=True,
    )

    notes = models.TextField(
        blank=True,
        default="",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-booking_date"]
        verbose_name = "Pregnancy"
        verbose_name_plural = "Pregnancies"

        indexes = [
            models.Index(
                fields=[
                    "patient",
                    "pregnancy_status",
                ]
            ),
        ]

    @property
    def is_active(self) -> bool:
        """
        Return True if the pregnancy
        is still ongoing.
        """

        return (
            self.pregnancy_status
            == PregnancyStatus.ONGOING
        )

    def __str__(self) -> str:
        """
        Return a readable representation.
        """

        return (
            f"{self.patient.patient_id}"
            f" ({self.booking_date})"
        )