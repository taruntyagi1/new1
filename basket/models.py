from oscar.apps.basket.abstract_models import (
    AbstractLine,
    AbstractBasket,
)
from oscar.core.utils import round_half_up
from decimal import Decimal


class Basket(AbstractBasket):
    """
    customize basket model
    """
    def save(self, *args, **kwargs):
        self.reset_offer_applications()
        super(self.__class__, self).save(*args, **kwargs)    


class Line(AbstractLine):
    """
    custom line model
    """
    @property
    def line_price_incl_tax_incl_discounts(self):
        # We use whichever discount value is set.  If the discount value was
        # calculated against the tax-exclusive prices, then the line price
        # including tax'
        # self.basket.reset_offer_applications()

        if self.line_price_incl_tax is not None and self._discount_incl_tax:
            if self.basket.vouchers and self.basket.vouchers.first() and self.basket.vouchers.first().max_discount_value and Decimal(self.basket.vouchers.first().max_discount_value) < self._discount_incl_tax:
                return max(0, self.line_price_incl_tax - Decimal(self.basket.vouchers.last().max_discount_value))
            else:
                return max(0, self.line_price_incl_tax - self._discount_incl_tax)

        elif self.line_price_excl_tax is not None and self._discount_excl_tax:
            
            # if self.basket.vouchers and self.basket.vouchers.first() and self.basket.vouchers.first().max_discount_value and Decimal(self.basket.vouchers.first().max_discount_value) < self._discount_excl_tax and self.basket.vouchers.first().benefit.type == 'Absolute':
            #     return max(0, self.line_price_excl_tax - Decimal(self.basket.vouchers.last().max_discount_value*self.quantity))

            if self.basket.vouchers and self.basket.vouchers.first() and self.basket.vouchers.first().max_discount_value and Decimal(self.basket.vouchers.first().max_discount_value) < self._discount_excl_tax:
                return max(0, self.line_price_excl_tax - Decimal(self.basket.vouchers.last().max_discount_value))

            else:
                return max(0, round_half_up((self.line_price_excl_tax - self._discount_excl_tax) / self._tax_ratio))
        
        return self.line_price_incl_tax
    
    @property
    def check_max_quantity(self):
        if self.product.stockrecords.first().num_allocated:
            num_allocated = self.product.stockrecords.first().num_allocated
        else:
            num_allocated = 0
        p_quantity = self.product.stockrecords.first().num_in_stock-num_allocated
      
        return p_quantity


    # @property
    # def line_price_incl_tax_incl_discounts(self):
    #     # We use whichever discount value is set.  If the discount value was
    #     # calculated against the tax-exclusive prices, then the line price
    #     # including tax
    #     # moin khan
    #     # self.basket.reset_offer_applications()
    #     if self.line_price_incl_tax is not None and self._discount_incl_tax:
    #         return max(0, self.line_price_incl_tax - self._discount_incl_tax)
    #     elif self.line_price_excl_tax is not None and self._discount_excl_tax:
    #         return max(0, round_half_up((self.line_price_excl_tax - self._discount_excl_tax) / self._tax_ratio))
    #         # return max(0, round_half_up((self.line_price_excl_tax - 200) / self._tax_ratio))
    #     return self.line_price_incl_tax    

from oscar.apps.basket.models import *  # noqa isort:skip
