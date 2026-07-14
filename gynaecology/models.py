from django.db import models

# Import Patient model.
from patients.models import Patient


class ConsultationType(models.TextChoices):
    """
    Types of gynaecology consultations.
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
    Stores gynaecology consultation records.
    """

    # Link consultation to a patient.
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="gynecology_consultations",
    )

    # Consultation date.
    consultation_date = models.DateField()

    # Type of consultation.
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

    # Examination findings.
    examination_findings = models.TextField(
        blank=True,
        default="",
    )

    # Diagnosis.
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

    def __str__(self):
        """
        Display consultation information.
        """

        return (
            f"{self.patient.patient_id} - "
            f"{self.consultation_type}"
        )