from django.db import models

from patients.models import Patient


class ConsultationType(models.TextChoices):
    """
    Allowed consultation types.
    """

    ROUTINE = "Routine Checkup", "Routine Checkup"
    MENSTRUAL = "Menstrual Disorder", "Menstrual Disorder"
    PELVIC_PAIN = "Pelvic Pain", "Pelvic Pain"
    VAGINAL_DISCHARGE = "Vaginal Discharge", "Vaginal Discharge"
    INFERTILITY = "Infertility", "Infertility"
    FIBROID = "Fibroid Evaluation", "Fibroid Evaluation"
    CERVICAL_SCREENING = (
        "Cervical Screening",
        "Cervical Screening",
    )


class GynecologyConsultation(models.Model):
    """
    Stores a patient's gynaecology
    consultation record.
    """

    # Patient receiving the consultation.
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="gynecology_consultations",
    )

    # Consultation date.
    consultation_date = models.DateField()

    # Consultation category.
    consultation_type = models.CharField(
        max_length=30,
        choices=ConsultationType.choices,
    )

    # Presenting complaint.
    presenting_complaint = models.TextField()

    # History of presenting complaint.
    history = models.TextField(
        blank=True,
        default="",
    )

    # Physical examination findings.
    examination_findings = models.TextField(
        blank=True,
        default="",
    )

    # Clinical diagnosis.
    diagnosis = models.TextField(
        blank=True,
        default="",
    )

    # Treatment provided.
    treatment = models.TextField(
        blank=True,
        default="",
    )

    # Follow-up plan.
    follow_up_plan = models.TextField(
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

    class Meta:
        ordering = ["-consultation_date", "-id"]
        verbose_name = (
            "Gynaecology Consultation"
        )
        verbose_name_plural = (
            "Gynaecology Consultations"
        )

    def __str__(self):
        """
        Human-readable representation.
        """

        return (
            f"{self.patient.patient_id} - "
            f"{self.consultation_type}"
        )