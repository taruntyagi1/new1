from django import template

from voucher.models import Voucher

register = template.Library()

@register.simple_tag
def order_amount(total_amount):
   total_amount = round(total_amount,2)
   return total_amount