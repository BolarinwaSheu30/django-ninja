import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from ninja.security import HttpBearer

# Secret key for signing JWTs.
SECRET_KEY = settings.SECRET_KEY

# Token expiry time.
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(user: User):
    """
    Generate a JWT access token.
    """

    expire = (
        datetime.utcnow()
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
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
        algorithm="HS256",
    )


def authenticate_user(
    username: str,
    password: str,
):
    """
    Validate username and password.
    """

    return authenticate(
        username=username,
        password=password,
    )




class JWTAuth(HttpBearer):
    """
    Authenticate requests using JWT.
    """

    def authenticate(self, request, token):
        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"],
            )

            user = User.objects.get(
                id=payload["user_id"]
            )

            return user

        except (
            jwt.ExpiredSignatureError,
            jwt.InvalidTokenError,
            User.DoesNotExist,
        ):
            return None

