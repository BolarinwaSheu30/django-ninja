from django.db import models
from django.contrib.auth.models import User


class UserRole(models.TextChoices):
    """
    Allowed staff roles.
    """

    ADMIN = "Admin", "Admin"
    DOCTOR = "Doctor", "Doctor"
    NURSE = "Nurse", "Nurse"
    RECEPTIONIST = "Receptionist", "Receptionist"
    LAB_STAFF = "Lab Staff", "Lab Staff"


class UserProfile(models.Model):
    """
    Extends Django's built-in User model
    with additional staff information.
    """

    # Linked Django user account.
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    # Staff role.
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.NURSE,
    )

    # Contact phone number.
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )

    class Meta:
        ordering = ["user__username"]
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        """
        Human-readable representation.
        """

        return (
            f"{self.user.username} "
            f"({self.role})"
        )