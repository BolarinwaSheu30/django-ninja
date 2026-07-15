from django.db import models
from django.contrib.auth.models import User


class UserRole(models.TextChoices):
    ADMIN = "Admin", "Admin"
    DOCTOR = "Doctor", "Doctor"
    NURSE = "Nurse", "Nurse"
    RECEPTIONIST = "Receptionist", "Receptionist"
    LAB_STAFF = "Lab Staff", "Lab Staff"


class UserProfile(models.Model):
    """
    Extends Django's built-in User model.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.NURSE,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"