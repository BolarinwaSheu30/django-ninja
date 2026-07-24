from ninja import Router

from django.contrib.auth.models import User

from config.common_schemas import (
    SuccessResponseSchema,
    ErrorResponseSchema,
)
from config.utils import (
    success_response,
    error_response,
)

from .auth import (
    JWTAuth,
    authenticate_user,
    create_access_token,
)
from .models import UserRole
from .permissions import require_roles
from .schemas import (
    LoginSchema,
    RegisterUserSchema,
)

auth = JWTAuth()

router = Router()



def _user_to_dict(user):
    """
    Convert a User model instance
    into a JSON-friendly dictionary.
    """

    return {
        "id": user.id,
        "username": user.username,
        "role": user.profile.role,
    }


@router.post(
    "/login",
    response={
        200: SuccessResponseSchema,
        401: ErrorResponseSchema,
    },
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
        return error_response(
            "Invalid username or password",
            401,
        )

    token = create_access_token(user)

    return success_response (
        "Login successful",
        {
            "access_token": token,
            "token_type": "bearer",
            "user": _user_to_dict(user),
        },
        )
        
            
        
    


@router.post(
    "/register",
    auth=auth,
    response={
        200: SuccessResponseSchema,
        400: ErrorResponseSchema,
        403: ErrorResponseSchema
    },
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
        username=payload.username,
    ).exists():
        return error_response(
            "Username already exists.",
            400,
        )
        

    # Create the Django user.
    user = User.objects.create_user(
        username=payload.username,
        password=payload.password,
    )

    # Update the linked profile.
    profile = user.profile
    profile.role = payload.role
    profile.phone_number = payload.phone_number
    profile.save(
        update_fields=[
            "role",
            "phone_number",
        ]
    )

    return success_response(
        "User created successfully.",
        _user_to_dict(user),
    )


@router.get(
    "/me",
    auth=auth,
    response={
        200: SuccessResponseSchema,
    },
)
def get_me(request):
    """
    Return information about
    the authenticated user.
    """

    user = request.auth

    return success_response(
        "User profile retrieved successfully",
        _user_to_dict(user),
    )
