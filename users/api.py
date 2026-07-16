from ninja import Router

from django.contrib.auth.models import User

from .models import UserRole

from .auth import (
    authenticate_user,
    create_access_token,
    JWTAuth,
)

from .schemas import (
    LoginSchema,
    TokenResponseSchema,
    UserProfileSchema,
    RegisterUserSchema,
)

from .permissions import require_roles

auth = JWTAuth()

router = Router()


@router.post(
    "/login",
    response=TokenResponseSchema,
)
def login(
    request,
    payload: LoginSchema,
):
    """
    Authenticate a user and
    return a JWT token.
    """

    user = authenticate_user(
        payload.username,
        payload.password,
    )

    if not user:
        return 401, {
            "detail": "Invalid credentials"
        }

    token = create_access_token(user)

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@router.post(
    "/register",
    auth=auth,
)
def register_user(
    request,
    payload: RegisterUserSchema,
):
    """
    Create a new staff user.
    Only Admin users can do this.
    """

    # Only Admin can create users.
    require_roles(
        request.auth,
        [UserRole.ADMIN],
    )

    # Check if username exists.
    if User.objects.filter(
        username=payload.username
    ).exists():
        return 400, {
            "detail": "Username already exists."
        }

    # Create the Django user.
    user = User.objects.create_user(
        username=payload.username,
        password=payload.password,
    )

    # Update the linked profile.
    profile = user.profile
    profile.role = payload.role
    profile.phone_number = payload.phone_number
    profile.save()

    return {
        "message": "User created successfully.",
        "username": user.username,
        "role": profile.role,
    }


@router.get(
    "/me",
    response=UserProfileSchema,
    auth=auth,
)
def get_current_user(request):
    """
    Return information about
    the authenticated user.
    """

    user = request.auth

    return {
        "username": user.username,
        "role": user.profile.role,
    }