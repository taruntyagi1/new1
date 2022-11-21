# django imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# oscar apps
from oscar.apps.address.abstract_models import *

class UserAddress(AbstractUserAddress):
    """
    Customized address model
    """
    ADDRESS_TYPE_CHOICE = (
        ('HM', 'Home Address'),
        ('OF', 'Office Address'),
        ('OTH', 'Other'),
    )

    address_type = models.CharField(
        _('Address Type'),
        max_length=5,
        choices=ADDRESS_TYPE_CHOICE,
        default='HM',
    )

    email = models.EmailField(
        _('Email'),
        null=True,
        blank=True,
    )

    alternate_mobile_number = PhoneNumberField(
        _('Alternate Mobile Number'),
        null=True,
        blank=True
    )

    @property
    def get_country_id(self):
        if self.country:
            return self.country.pk
        else:
            return None    

from oscar.apps.address.models import *  # noqa isort:skip
