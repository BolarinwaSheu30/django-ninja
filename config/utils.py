"""
Reusable helper functions for API responses.
"""

from typing import Any


def success_response(
    message: str,
    data: Any = None,
) -> dict:
    """
    Build a standardized successful
    API response.

    Args:
        message:
            Human-readable success message.

        data:
            Response payload.

    Returns:
        Standard success response.
    """

    return {
        "status": "success",
        "message": message,
        "data": data,
    }


def error_response(
    message: str,
    status_code: int = 400,
) -> tuple[int, dict]:
    """
    Build a standardized error
    API response.

    Args:
        message:
            Human-readable error message.

        status_code:
            HTTP status code.

    Returns:
        Tuple containing the HTTP
        status code and response body.
    """

    return (
        status_code,
        {
            "status": "error",
            "message": message,
            "data": None,
        },
    )