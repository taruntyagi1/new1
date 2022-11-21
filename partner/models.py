# oscar imports
from oscar.apps.partner.abstract_models import *

# django imports
from django.utils.translation import gettext_lazy as _

class StockRecord(AbstractStockRecord):
    """
    customized stock record
    """

    partner = models.ForeignKey(
        'partner.Partner',
        on_delete=models.CASCADE,
        verbose_name=_("Partner"),
        related_name='stockrecords',
        null=True,
        blank=True,
    )

    @property
    def get_percentage_discount(self):
        if self.price_retail and self.price_excl_tax:
            discount =  self.price_retail - self.price_excl_tax
            percentage_discount = (discount*100)/self.price_retail
            return int(percentage_discount)

from oscar.apps.partner.models import *  # noqa isort:skip