from ninja import Schema


class RegisterUserSchema(Schema):
    """
    Create a new staff user.
    """

    username: str
    password: str
    role: str
    phone_number: str = ""


class LoginSchema(Schema):
    """
    User login request.
    """

    username: str
    password: str


class TokenResponseSchema(Schema):
    """
    JWT token response.
    """

    access_token: str
    token_type: str = "bearer"


class UserProfileSchema(Schema):
    """
    Authenticated user information.
    """

    username: str
    role: str


class UserInfoSchema(Schema):
    """
    Basic user information returned after login.
    """

    username: str
    role: str


class LoginDataSchema(Schema):
    """
    Login payload containing token and user info.
    """

    access_token: str
    token_type: str
    user: UserInfoSchema


class LoginResponseSchema(Schema):
    """
    Standardized login response.
    """

    status: str
    message: str
    data: LoginDataSchema