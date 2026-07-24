"""
Authentication utilities for JWT-based authentication.
"""

from datetime import timedelta

import jwt

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils import timezone

from ninja.security import HttpBearer

from config.settings import SECRET_KEY


# JWT configuration.

JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(
    user: User,
) -> str:
    """
    Generate a JWT access token.
    """

    expire = (
        timezone.now()
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
        )
    )

    payload = {
        "user_id": user.id,
        "username": user.username,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def authenticate_user(
    username: str,
    password: str,
) -> User | None:
    """
    Authenticate a user using
    Django's authentication system.
    """

    return authenticate(
        username=username,
        password=password,
    )


class JWTAuth(HttpBearer):
    """
    Authenticate requests using JWT tokens.
    """

    def authenticate(
        self,
        request,
        token: str,
    ) -> User | None:
        """
        Validate the supplied JWT token
        and return the authenticated user.
        """

        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=[JWT_ALGORITHM],
            )

            return User.objects.get(
                id=payload["user_id"],
            )

        except (
            jwt.ExpiredSignatureError,
            jwt.InvalidTokenError,
            User.DoesNotExist,
        ):
            return None