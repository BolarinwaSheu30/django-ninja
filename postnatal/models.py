"""
Postnatal Care models.
"""

from django.db import models

from deliveries.models import Delivery


class BreastfeedingStatus(models.TextChoices):
    """
    Available breastfeeding status options.
    """

    EXCLUSIVE = "Exclusive", "Exclusive"
    MIXED = "Mixed", "Mixed"
    NOT_BREASTFEEDING = (
        "Not Breastfeeding",
        "Not Breastfeeding",
    )


class PostnatalVisit(models.Model):
    """
    Stores information collected during
    a postnatal care visit.
    """

    # Related delivery.
    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
        related_name="postnatal_visits",
    )

    # Visit details.
    visit_date = models.DateField()

    visit_number = models.PositiveIntegerField()

    # Maternal observations.
    blood_pressure = models.CharField(
        max_length=20,
    )

    temperature_c = models.DecimalField(
        max_digits=4,
        decimal_places=1,
    )

    pulse_rate = models.PositiveIntegerField()

    lochia = models.CharField(
        max_length=50,
        blank=True,
        default="",
    )

    wound_healing = models.CharField(
        max_length=100,
        blank=True,
        default="",
    )

    # Infant assessment.
    baby_weight_kg = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    feeding_well = models.BooleanField(
        default=True,
    )

    immunization_given = models.BooleanField(
        default=False,
    )

    # Breastfeeding.
    breastfeeding_status = models.CharField(
        max_length=30,
        choices=BreastfeedingStatus.choices,
    )

    # Family planning.
    family_planning_counseled = models.BooleanField(
        default=False,
    )

    # Follow-up.
    next_appointment_date = models.DateField(
        null=True,
        blank=True,
    )

    # Additional notes.
    notes = models.TextField(
        blank=True,
        default="",
    )

    # Audit information.
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-visit_date", "-id"]
        verbose_name = "Postnatal Visit"
        verbose_name_plural = "Postnatal Visits"

    def __str__(self):
        """
        Return a readable representation.
        """

        return (
            f"{self.delivery.pregnancy.patient.patient_id} "
            f"- PNC Visit {self.visit_number}"
        )