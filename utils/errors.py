"""
File for error formatting
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
from pydantic import ValidationError

from models.response_models import ErrorResponse


def validation_error_serializer(error: dict):
    """
    Serializer for error responses
    :param error:
    :return:
    """
    return ErrorResponse(message=error["msg"], type=error["type"], input=error["input"]).dict()


def format_validation_error(e: ValidationError) -> list:
    """
    Format error for validation error
    :param e: ValidationError object
    :return: list of dictionaries with errors
    """
    return [validation_error_serializer(error) for error in e.errors()]
