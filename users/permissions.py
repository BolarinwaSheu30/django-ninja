from ninja.errors import HttpError

from .models import UserRole


def require_roles(user, allowed_roles):
    """
    Ensure the authenticated user
    has one of the allowed roles.
    """

    user_role = user.profile.role

    if user_role not in allowed_roles:
        raise HttpError(
            403,
            "You do not have permission "
            "to perform this action.",
        )