from django.db import models

# Import the Pregnancy model.
from pregnancies.models import Pregnancy


class AntenatalVisit(models.Model):
    """
    Stores information collected during
    an antenatal clinic visit.
    """

    # Link the visit to a pregnancy.
    pregnancy = models.ForeignKey(
        Pregnancy,
        on_delete=models.CASCADE,
        related_name="antenatal_visits",
    )

    # Visit date.
    visit_date = models.DateField()

    # Visit number (1st visit, 2nd visit, etc.).
    visit_number = models.PositiveIntegerField()

    # Maternal weight in kilograms.
    weight_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    # Blood pressure.
    blood_pressure = models.CharField(
        max_length=20,
    )

    # Fetal heart rate.
    fetal_heart_rate = models.PositiveIntegerField()

    # Maternal temperature in Celsius.
    temperature_c = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    # Maternal pulse rate.
    pulse_rate = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    # Fundal height in centimeters.
    fundal_height_cm = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    # Whether fetal movement is present.
    fetal_movement_present = models.BooleanField(
        default=True,
    )

    # Urine protein result.
    urine_protein = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )

    # Urine glucose result.
    urine_glucose = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )

    # Next clinic appointment.
    next_appointment_date = models.DateField(
        null=True,
        blank=True,
    )

    # Clinical notes.
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
        Display visit information.
        """

        return (
            f"{self.pregnancy.patient.patient_id} - "
            f"Visit {self.visit_number}"
        )