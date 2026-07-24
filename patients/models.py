"""
Patient model.
"""

from django.db import models
from django.utils import timezone


class Gender(models.TextChoices):
    """
    Patient gender choices.
    """

    MALE = "Male", "Male"
    FEMALE = "Female", "Female"


class BloodGroup(models.TextChoices):
    """
    Blood group choices.
    """

    A_POSITIVE = "A+", "A+"
    A_NEGATIVE = "A-", "A-"
    B_POSITIVE = "B+", "B+"
    B_NEGATIVE = "B-", "B-"
    AB_POSITIVE = "AB+", "AB+"
    AB_NEGATIVE = "AB-", "AB-"
    O_POSITIVE = "O+", "O+"
    O_NEGATIVE = "O-", "O-"


class MaritalStatus(models.TextChoices):
    """
    Marital status choices.
    """

    SINGLE = "Single", "Single"
    MARRIED = "Married", "Married"
    DIVORCED = "Divorced", "Divorced"
    WIDOWED = "Widowed", "Widowed"


class Patient(models.Model):
    """
    Stores demographic information
    about a patient.
    """

    patient_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        db_index=True,
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
        db_index=True,
    )

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        blank=True,
        default="",
    )

    blood_group = models.CharField(
        max_length=5,
        choices=BloodGroup.choices,
        blank=True,
        default="",
    )

    marital_status = models.CharField(
        max_length=20,
        choices=MaritalStatus.choices,
        blank=True,
        default="",
    )

    occupation = models.CharField(
        max_length=100,
        blank=True,
        default="",
    )

    next_of_kin_name = models.CharField(
        max_length=100,
        blank=True,
        default="",
    )

    next_of_kin_phone = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )

    phone_number = models.CharField(
        max_length=20,
        db_index=True,
    )

    address = models.TextField()

    emergency_contact = models.CharField(
        max_length=100,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    @property
    def full_name(self) -> str:
        """
        Return the patient's full name.
        """

        return f"{self.first_name} {self.last_name}"

    def save(
        self,
        *args,
        **kwargs,
    ) -> None:
        """
        Automatically generate a unique
        patient ID.
        """

        if not self.patient_id:
            current_year = timezone.now().year

            last_patient = (
                self.__class__.objects
                .order_by("id")
                .last()
            )

            next_number = (
                last_patient.id + 1
                if last_patient
                else 1
            )

            self.patient_id = (
                f"MC-{current_year}-{next_number:04d}"
            )

        super().save(
            *args,
            **kwargs,
        )

    def __str__(self) -> str:
        """
        Return the patient's full name.
        """

        return (
            f"{self.patient_id} - "
            f"{self.full_name}"
        )