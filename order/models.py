# django imports
from django.utils.translation import gettext_lazy as _
from django.db import models
# oscar imports
from oscar.apps.order.abstract_models import *

class Order(AbstractOrder):
    """
    Extended order model
    """
    payment_done = models.BooleanField(
        _('Payment Done'),
        default=False,
    )

    transaction_number = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    

    @property
    def basket_total_before_discounts_incl_tax(self):
        """
        Return basket total including tax but before discounts are applied
        """
        total = D('0.00')
        for line in self.lines.all():
            total += line.line_price_before_discounts_incl_tax
        return total

from oscar.apps.order.models import *  # noqa isort:skip
