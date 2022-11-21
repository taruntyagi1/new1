"""
    Custom Authentication by Overriding the Django BaseBacked/Object

    Object is Override to authenticate the user via OTP as well
"""

# python imports

# django imports
from django.contrib.auth import get_user_model

# local imports
from .models import UserOTP

class MobileOTPAuthenticationBackEnd(object):
    """
    Authenticates user based on given mobile_number and otp.
    """

    def authenticate(self, request, mobile_number, otp, **kwargs):
        
        try:
            user = get_user_model().objects.select_related('otp').get(mobile_number=mobile_number)
        except get_user_model().DoesNotExist:
            return None
        else:
            if user.is_active \
                and hasattr(user, 'otp') \
                and user.otp.validate_otp(otp, UserOTP.LOGIN_VERIFICATION):
                return user
            return None

        return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id, is_active=True)
        except get_user_model().DoesNotExist:
            return None


class MobileOnlyAuthenticationBackEnd(object):
    """
    Authenticates user based on given mobile_number and otp.
    """

    def authenticate(self, request, mobile_number, **kwargs):
        if not kwargs.get('strict_login_with_otp'):
            try:
                user = get_user_model().objects.get(mobile_number=mobile_number)
            except get_user_model().DoesNotExist:
                return None
            else:
                if user.is_active:
                    return user
                return None
        return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id, is_active=True)
        except get_user_model().DoesNotExist:
            return None