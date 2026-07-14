from django.db import models

# Import Delivery model.
from deliveries.models import Delivery


class BreastfeedingStatus(models.TextChoices):
    """
    Breastfeeding status options.
    """

    EXCLUSIVE = "Exclusive", "Exclusive"
    MIXED = "Mixed", "Mixed"
    NOT_BREASTFEEDING = (
        "Not Breastfeeding",
        "Not Breastfeeding",
    )


class PostnatalVisit(models.Model):
    """
    Stores postnatal care visit information.
    """

    # Link visit to a delivery.
    delivery = models.ForeignKey(
        Delivery,
        on_delete=models.CASCADE,
        related_name="postnatal_visits",
    )

    # Date of the postnatal visit.
    visit_date = models.DateField()

    # Visit number.
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

    # Lochia assessment.
    lochia = models.CharField(
        max_length=50,
        blank=True,
        default="",
    )

    # Breastfeeding status.
    breastfeeding_status = models.CharField(
        max_length=30,
        choices=BreastfeedingStatus.choices,
    )

    # Wound healing assessment.
    wound_healing = models.CharField(
        max_length=100,
        blank=True,
        default="",
    )

    # Baby assessment.
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

    # Family planning counseling.
    family_planning_counseled = models.BooleanField(
        default=False,
    )

    # Next appointment.
    next_appointment_date = models.DateField(
        null=True,
        blank=True,
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
        Display postnatal visit information.
        """

        return (
            f"{self.delivery.pregnancy.patient.patient_id} - "
            f"PNC Visit {self.visit_number}"
        )