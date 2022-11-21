
from oscar.apps.voucher.abstract_models import AbstractVoucher
from django.utils.translation import gettext_lazy as _
from django.db import models

class Voucher(AbstractVoucher):
    created_from = models.CharField(
        max_length=100,
        default="IE"
    )

    max_discount_value = models.FloatField(
        _('Max Discount'),
       default=0,
       null=True,
       blank=True
    )

from oscar.apps.voucher.models import *  # noqa isort:skip
