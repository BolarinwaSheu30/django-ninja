from ninja import Router

from .auth import (
    authenticate_user,
    create_access_token,
    JWTAuth,
)

from .schemas import (
    LoginSchema,
    TokenResponseSchema,
    UserProfileSchema,
)

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


@router.get(
    "/me",
    response=UserProfileSchema,
    auth = auth,
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