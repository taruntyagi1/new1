# oscar imports
from ipdb.__main__ import set_trace
from django.utils.translation import gettext_lazy as _
from oscar.apps.dashboard.catalogue.formsets import *
# inner app imports
from catalogue.models import Product

# local imports
from .forms import CustomStockRecordForm

BaseStockRecordFormSet = inlineformset_factory(
    Product, StockRecord, form=CustomStockRecordForm, extra=1,)

class CustomStockRecordFormSet(BaseStockRecordFormSet, StockRecordFormSet):
    """
    CustomStockRecord Formset
    """
    def clean(self):
        """
        If the user isn't a staff user, this validation ensures that at least
        one stock record's partner is associated with a users partners.
        """
        if any(self.errors):
            return

        if self.instance.structure=='child' and (not self.forms[0].cleaned_data or (self.forms[0].cleaned_data and self.forms[0].cleaned_data.get('DELETE'))):
            raise exceptions.ValidationError(
                _('If you are adding child product then you should add at least one stock record')
            )

        if self.require_user_stockrecord:
            stockrecord_partners = set([form.cleaned_data.get('partner', None)
                                        for form in self.forms])
            user_partners = set(self.user.partners.all())
            if not user_partners & stockrecord_partners:
                raise exceptions.ValidationError(
                    _("At least one stock record must be set to a partner that"
                      " you're associated with."))