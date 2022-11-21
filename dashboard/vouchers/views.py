from oscar.apps.dashboard.vouchers.views import VoucherCreateView, VoucherListView, VoucherStatsView, VoucherUpdateView
from dashboard.vouchers.forms import CustomVoucherForm
from voucher.models import Voucher

from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from oscar.apps.voucher.utils import get_offer_name
from oscar.core.loading import get_class, get_model


ConditionalOffer = get_model('offer', 'ConditionalOffer')
Benefit = get_model('offer', 'Benefit')
Condition = get_model('offer', 'Condition')


class VoucherCreateView(VoucherCreateView):
    """
    View for create Voucher
    """
    model=Voucher
    form_class = CustomVoucherForm
    template_name = 'vouchers/voucher_form.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = _('Create voucher')
        return ctx

    def get_initial(self):
        return dict(
            exclusive=True
        )

    @transaction.atomic()
    def form_valid(self, form):
        # Create offer and benefit
        condition = Condition.objects.create(
            range=form.cleaned_data['benefit_range'],
            type=Condition.COUNT,
            value=1
        )
        benefit = Benefit.objects.create(
            range=form.cleaned_data['benefit_range'],
            type=form.cleaned_data['benefit_type'],
            value=form.cleaned_data['benefit_value']
        )
        name = form.cleaned_data['name']
        offer = ConditionalOffer.objects.create(
            name=get_offer_name(name),
            offer_type=ConditionalOffer.VOUCHER,
            benefit=benefit,
            condition=condition,
            exclusive=form.cleaned_data['exclusive'],
        )
        voucher = Voucher.objects.create(
            name=name,
            code=form.cleaned_data['code'],
            usage=form.cleaned_data['usage'],
            start_datetime=form.cleaned_data['start_datetime'],
            end_datetime=form.cleaned_data['end_datetime'],
            max_discount_value=form.cleaned_data['max_discount_value']
        )
        voucher.offers.add(offer)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, _("Voucher created"))
        return reverse('dashboard:voucher-list')


class VoucherListView(VoucherListView):
    """
    Voucher List View
    """

    template_name = 'vouchers/voucher_list.html'


class VoucherDetailView(VoucherStatsView):
    """
    Voucher detail View
    """

    template_name = 'vouchers/voucher_detail.html'



class VoucherUpdateView(VoucherUpdateView):
    template_name = 'vouchers/voucher_form.html'
    model = Voucher
    form_class = CustomVoucherForm

    def get_voucher(self):
        if not hasattr(self, 'voucher'):
            self.voucher = Voucher.objects.get(id=self.kwargs['pk'])
        return self.voucher

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.voucher.name
        ctx['voucher'] = self.voucher
        return ctx

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['voucher'] = self.get_voucher()
        return kwargs

    def get_initial(self):
        voucher = self.get_voucher()
        offer = voucher.offers.all()[0]
        benefit = offer.benefit
        return {
            'name': voucher.name,
            'code': voucher.code,
            'start_datetime': voucher.start_datetime,
            'end_datetime': voucher.end_datetime,
            'usage': voucher.usage,
            'benefit_type': benefit.type,
            'benefit_range': benefit.range,
            'benefit_value': benefit.value,
            'exclusive': offer.exclusive,
            'max_discount_value':voucher.max_discount_value
        }

    @transaction.atomic()
    def form_valid(self, form):
        voucher = self.get_voucher()
        voucher.name = form.cleaned_data['name']
        voucher.code = form.cleaned_data['code']
        voucher.usage = form.cleaned_data['usage']
        voucher.start_datetime = form.cleaned_data['start_datetime']
        voucher.end_datetime = form.cleaned_data['end_datetime']
        voucher.max_discount_value = form.cleaned_data['max_discount_value']
        voucher.save()

        offer = voucher.offers.all()[0]
        offer.condition.range = form.cleaned_data['benefit_range']
        offer.condition.save()

        offer.exclusive = form.cleaned_data['exclusive']
        offer.name = get_offer_name(voucher.name)
        offer.save()

        benefit = voucher.benefit
        benefit.range = form.cleaned_data['benefit_range']
        benefit.type = form.cleaned_data['benefit_type']
        benefit.value = form.cleaned_data['benefit_value']
        benefit.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, _("Voucher updated"))
        return reverse('dashboard:voucher-list')

