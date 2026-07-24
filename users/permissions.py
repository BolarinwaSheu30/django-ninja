"""
Authorization helpers.
"""

from typing import Iterable

from ninja.errors import HttpError

from .models import UserRole


def require_roles(
    user,
    allowed_roles: Iterable[str],
) -> None:
    """
    Ensure the authenticated user
    has one of the allowed roles.

    Args:
        user:
            The authenticated Django user.

        allowed_roles:
            Collection of roles permitted
            to access the endpoint.

    Raises:
        HttpError:
            If the user's role is not allowed.
    """

    if user.profile.role not in allowed_roles:
        raise HttpError(
            403,
            "You do not have permission "
            "to perform this action.",
        )