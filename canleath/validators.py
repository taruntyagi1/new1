from django.core.validators import RegexValidator

from .messages import VALIDATION_ERROR_MESSAGES

NAME_VALIDATOR = RegexValidator(
    regex=r'^[a-zA-Z.\s]{1,150}$',
    message=VALIDATION_ERROR_MESSAGES['INVALID_NAME'],
    code='INVALID_NAME'
)

MobileNumberValidator = RegexValidator(
    regex='^[-+]?[0-9]+$',
    message=VALIDATION_ERROR_MESSAGES['INVALID_MOBILE_NUMBER'],
    code='INVALID_MOBILE_NUMBER'
)