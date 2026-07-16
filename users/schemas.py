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

class RegisterUserSchema(Schema):
    """
    Create a new staff user.
    """

    username: str
    password: str
    role: str
    phone_number: str = ""