"""
Schemas for User Authentication.
"""

from ninja import Schema


class RegisterUserSchema(Schema):
    """
    Data required to create
    a new staff user.
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


class UserProfileSchema(Schema):
    """
    Authenticated user profile.
    """

    username: str

    role: str


class UserInfoSchema(Schema):
    """
    Basic user information.

    Used inside login responses.
    """

    username: str

    role: str