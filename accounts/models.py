# python imports
import os
import uuid
import datetime
import requests
import json


# django imports
from django.core.validators import FileExtensionValidator

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

# oscar imports
from oscar.apps.customer.abstract_models import AbstractUser, UserManager

# inner app imports
from canleath.messages import HELP_TEXTS, SMS_TEXTS
from canleath.utils import get_first_and_last_name, send_sms_api

# third party imports
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token

# local imports
from .managers import UserManager

def get_profile_picture(instance, filename):
    """Set the profile picture Location in Account media"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    location = os.path.join('user/', 'profile/')
    return os.path.join(location, filename)

# Create your models here.

class User(AbstractUser):
    """
    customized user model
    """

    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    mobile_number = PhoneNumberField(
        _('Mobile Number'),
        unique=True,
    )

    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)

    gender = models.CharField(
        _('Male/Female'),
        choices=GENDERS,
        max_length=1,
        null=True,
        blank=True,
    )

    dob = models.DateField(
        _("DOB"),
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        _('Profile Picture'),
        validators=[FileExtensionValidator(allowed_extensions=[ 'JPEG', 'PNG', 'JPG'])],
        help_text=HELP_TEXTS['PROFILE PICTURE'],
        upload_to=get_profile_picture,
        blank=True,
        null=True,
    )

    terms_and_conditions = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = [
        'email',
    ]

    @property
    def full_name(self):
        return self.get_full_name()

    def __str__(self):
        return self.email or self.sys_id

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)    

    def get_short_name(self):
        return self.first_name

    # def send_otp(self, purpose, country_code, otp):
    #     """
    #     Sends OTP As Sms On User Mobile.
    #     """
    #     send_sms_api([self.usable_mobile], purpose, country_code, otp, user=self)
    @property
    def sys_id(self):
        return 'USER{}'.format(str(self.pk + 1000).zfill(6))    

    @property
    def name(self):
        return self.get_full_name()

    @name.setter
    def name(self, full_name):
        self.first_name, self.last_name = get_first_and_last_name(full_name)   



class UserOTP(models.Model):
    """
    Handles Users OTPs
    """

    MOBILE_VERIFICATION = 'MV'
    LOGIN_VERIFICATION = 'LO'

    OTP_PURPOSE = (
        (MOBILE_VERIFICATION, 'Mobile Verification'),
        (LOGIN_VERIFICATION, 'Login'),
    )

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='otp',
        null=True,
        blank=True,
    )

    mobile_number = PhoneNumberField(
        _('mobile number'),
        null=True,
        blank=True,
    )

    password = models.CharField(
        _('password'),
        max_length=6,
        blank=True,
        null=True
    )

    last_modified = models.DateTimeField(auto_now=True)

    purpose = models.CharField(
        max_length=2,
        choices=OTP_PURPOSE,
        blank=True,
        null=True,
        default='MV'
    )

    def __str__(self):
        return self.sys_id

    @property
    def sys_id(self):
        return 'OTP{}'.format(str(self.pk + 1000).zfill(6))

    @classmethod
    def make_random_otp(cls):
        return get_random_string(length=6, allowed_chars='0123456789')

    def get_otp(self, purpose):
        """
        If Otp Is Not Expired The Return The Old Otp Else Generate New.
        """
        if(not self.password or
           (timezone.now() > self.last_modified + timezone.timedelta(minutes=settings.OTP_VALIDITY)) or
           purpose != self.purpose):
            self.password = '000000' if settings.DEBUG else self.__class__.make_random_otp()
            self.purpose = purpose
            self.save()
        return self.password

    def send_otp(self, purpose, *args, **kwargs):
        """
        Send Otp To User
        """
        if purpose == UserOTP.MOBILE_VERIFICATION:
            purpose_display = 'Mobile Verification'
            # message = SMS_TEXTS['OTP'].format(otp=self.get_otp(purpose), purpose=purpose_display)
            send_sms_api(self.mobile_number, self.get_otp(purpose))

        elif purpose == UserOTP.LOGIN_VERIFICATION:
            purpose_display = 'Login'
            # message = SMS_TEXTS['OTP'].format(otp=self.get_otp(purpose), purpose=purpose_display)
            send_sms_api(self.mobile_number, self.get_otp(purpose))

    def validate_otp(self, otp, purpose):
        if otp == self.password \
                and (timezone.now() < self.last_modified + timezone.timedelta(minutes=settings.OTP_VALIDITY)) \
                and purpose == self.purpose:
            self.password = None
            self.purpose = None
            self.save()
            return True
        return False

    def get_auth_token(self):
        """
        Get Or Create Token Key For User.
        """
        if hasattr(self, 'auth_token'):
            key = self.auth_token.generate_key()
            Token.objects.filter(user=self).update(key=key)
            return key
        else:
            token = Token.objects.create(user=self)
            return token.key
