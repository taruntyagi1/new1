# oscar imports
from oscar.apps.dashboard.vouchers import forms as base_forms
from django import forms

from voucher.models import Voucher

class CustomVoucherForm(base_forms.VoucherForm):
    """
    Customized voucher Form
    """
    max_discount_value = forms.FloatField(required=False)
    class Meta:
        model = Voucher
        fields = (
            'name',
            'code',
            'start_datetime',
            'end_datetime',
            'usage',
            'benefit_range',
            'benefit_type',
            'benefit_value',
            'max_discount_value'
        )

    def __init__(self, *args, **kwargs):
        super(CustomVoucherForm, self).__init__(*args, **kwargs)
       