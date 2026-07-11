from django.db import models
from django.utils import timezone


class Patient(models.Model):
    """
    Stores demographic information
    about a patient.
    """

    # Unique hospital patient identifier
    patient_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
    )

    # Patient first name
    first_name = models.CharField(
        max_length=100
    )

    # Patient last name
    last_name = models.CharField(
        max_length=100
    )

    # Date of birth
    date_of_birth = models.DateField()


    # Gender
    gender = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    # Blood group
    blood_group = models.CharField(
        max_length=5,
        blank=True,
        default=""
    )

    # Marital status
    marital_status = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    # Occupation
    occupation = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    # Next of kin name
    next_of_kin_name = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    # Next of kin phone number
    next_of_kin_phone = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    

    # Phone number
    phone_number = models.CharField(
        max_length=20
    )

    # Home address
    address = models.TextField()

    # Emergency contact
    emergency_contact = models.CharField(
        max_length=100
    )

    # Record creation timestamp
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        """
        Automatically generate a patient ID
        when creating a new patient.
        """

        # Only generate an ID for new patients
        if not self.patient_id:

           # Current year
           current_year = timezone.now().year

           # Count existing patients
           patient_count = Patient.objects.count() + 1

           # Generate ID
           self.patient_id = (
                f"MC-{current_year}-{patient_count:04d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        """
        Display patient name in admin panel.
        """

        return f"{self.first_name} {self.last_name}"