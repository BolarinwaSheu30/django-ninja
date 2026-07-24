"""
Antenatal visit model.
"""

from django.db import models

from pregnancies.models import Pregnancy


class AntenatalVisit(models.Model):
    """
    Stores information collected during
    an antenatal clinic visit.
    """

    pregnancy = models.ForeignKey(
        Pregnancy,
        on_delete=models.CASCADE,
        related_name="antenatal_visits",
    )

    visit_date = models.DateField(
        db_index=True,
    )

    visit_number = models.PositiveIntegerField()

    weight_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    blood_pressure = models.CharField(
        max_length=20,
    )

    fetal_heart_rate = models.PositiveIntegerField()

    temperature_c = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    pulse_rate = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    fundal_height_cm = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    fetal_movement_present = models.BooleanField(
        default=True,
    )

    urine_protein = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )

    urine_glucose = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )

    next_appointment_date = models.DateField(
        null=True,
        blank=True,
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
            "-visit_date",
        ]

        verbose_name = "Antenatal Visit"

        verbose_name_plural = (
            "Antenatal Visits"
        )

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "pregnancy",
                    "visit_number",
                ],
                name=(
                    "unique_antenatal_visit_number"
                ),
            ),
        ]

        indexes = [
            models.Index(
                fields=[
                    "pregnancy",
                    "visit_date",
                ],
            ),
        ]

    @property
    def patient(self):
        """
        Return the patient associated
        with this visit.
        """

        return self.pregnancy.patient

    def __str__(self) -> str:
        """
        Return a readable
        representation.
        """

        return (
            f"{self.patient.patient_id} "
            f"- Visit {self.visit_number}"
        )