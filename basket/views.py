# django import
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# oscar imports
from django.contrib import messages
from oscar.apps.basket.views import BasketView, VoucherAddView
from oscar.core.loading import get_class, get_model
from oscar.core import ajax
from oscar.core.utils import redirect_to_referrer, safe_referrer
from voucher.models import Voucher
from django.views.generic import TemplateView
 
# local import
from .utils import BasketMessageGenerator

Applicator = get_class('offer.applicator', 'Applicator')

import pdb
class CustomBasketView(BasketView):
    """
    Customized basket View
    """

    template_name = 'basket/basket.html'
    
    def get_queryset(self):
        """
        Return list of :py:class:`Line <oscar.apps.basket.abstract_models.AbstractLine>`
        instances associated with the current basket.
        """  # noqa: E501
        
        return self.request.basket.all_lines().order_by('-date_updated')


    def formset_valid(self, formset):
        # Store offers before any changes are made so we can inform the user of
        # any changes
        offers_before = self.request.basket.applied_offers()
        save_for_later = False

        # Keep a list of messages - we don't immediately call
        # django.contrib.messages as we may be returning an AJAX response in
        # which case we pass the messages back in a JSON payload.
        flash_messages = ajax.FlashMessages()

        for form in formset:
            if (hasattr(form, 'cleaned_data')
                    and form.cleaned_data.get('save_for_later', False)):
                line = form.instance
               
                if self.request.user.is_authenticated:
                    self.move_line_to_saved_basket(line)

                    msg = render_to_string(
                        'oscar/basket/messages/line_saved.html',
                        {'line': line})
                    flash_messages.info(msg)

                    save_for_later = True
                else:
                    msg = _("You can't save an item for later if you're "
                            "not logged in!")
                    flash_messages.error(msg)
                    return redirect(self.get_success_url())

        if save_for_later:
            # No need to call super if we're moving lines to the saved basket
            response = redirect(self.get_success_url())
        else:
            # Save changes to basket as per normal
            response = super().formset_valid(formset)

        # If AJAX submission, don't redirect but reload the basket content HTML
        if self.request.is_ajax():
            
            # Reload basket and apply offers again
            self.request.basket = get_model('basket', 'Basket').objects.get(
                id=self.request.basket.id)
            self.request.basket.strategy = self.request.strategy
            Applicator().apply(self.request.basket, self.request.user,
                               self.request)
            offers_after = self.request.basket.applied_offers()

            for level, msg in BasketMessageGenerator().get_messages(
                    self.request.basket, offers_before, offers_after, include_buttons=False):
                flash_messages.add_message(level, msg)

            # Reload formset - we have to remove the POST fields from the
            # kwargs as, if they are left in, the formset won't construct
            # correctly as there will be a state mismatch between the
            # management form and the database.
            kwargs = self.get_formset_kwargs()
            del kwargs['data']
            del kwargs['files']
            if 'queryset' in kwargs:
                del kwargs['queryset']
            formset = self.get_formset()(queryset=self.get_queryset(),
                                         **kwargs)
            ctx = self.get_context_data(formset=formset,
                                        basket=self.request.basket)
            return self.json_response(ctx, flash_messages)

        BasketMessageGenerator().apply_messages(self.request, offers_before)
    
        return response

    def get_context_data(self, **kwargs):
        # pdb.set_trace()
        context = super(CustomBasketView, self).get_context_data(**kwargs)
        now = timezone.now()
        context['voucher_list'] = Voucher.objects.filter(start_datetime__lte=now, end_datetime__gte=now)
        try:
            context['applied_voucher_list'] = [voucher.code for voucher in self.request.basket.vouchers.all() if hasattr(self.request.basket, 'vouchers')]
        except Exception as e:
            pass  
        # customer=self.request.user
        # context['delivery_charge'] = CourierServiceability(customer)
        return context



class VoucherAddView(VoucherAddView):
  
    def form_valid(self, form):
        # import ipdb;ipdb.set_trace()
		

        code = form.cleaned_data['code']
        if not self.request.basket.id:
            return redirect_to_referrer(self.request, 'basket:summary')
       
            

        if self.request.basket.contains_voucher(code):
            messages.error(
                self.request,
                _("You have already added the '%(code)s' voucher to "
                  "your basket") % {'code': code})
        else:
            try:
                voucher = self.voucher_model._default_manager.get(code=code)
                
                
            except self.voucher_model.DoesNotExist:
                messages.error(
                    self.request,
                    _("No voucher found with code '%(code)s'") % {
                        'code': code})
            else:
              
                if voucher.benefit.type == 'Absolute' and float(voucher.benefit.value) > float(self.request.basket.total_incl_tax):
                    messages.error(
                        self.request,
                        _('Coupon Code not applicable'))
                else:
                    self.apply_voucher_to_basket(voucher)
        return redirect_to_referrer(self.request, 'basket:summary')


class BasketItemView(BasketView):
    """
    Customized basket View
    """

    template_name = 'basket/partials/basket_items.html'
    
    def get_queryset(self):
        """
        Return list of :py:class:`Line <oscar.apps.basket.abstract_models.AbstractLine>`
        instances associated with the current basket.
        """  # noqa: E501
        return self.request.basket.all_lines().order_by('-date_updated')


    def formset_valid(self, formset):
        # Store offers before any changes are made so we can inform the user of
        # any changes
        offers_before = self.request.basket.applied_offers()
        save_for_later = False

        # Keep a list of messages - we don't immediately call
        # django.contrib.messages as we may be returning an AJAX response in
        # which case we pass the messages back in a JSON payload.
        flash_messages = ajax.FlashMessages()

        for form in formset:
            if (hasattr(form, 'cleaned_data')
                    and form.cleaned_data.get('save_for_later', False)):
                line = form.instance
               
                if self.request.user.is_authenticated:
                    self.move_line_to_saved_basket(line)

                    msg = render_to_string(
                        'oscar/basket/messages/line_saved.html',
                        {'line': line})
                    flash_messages.info(msg)

                    save_for_later = True
                else:
                    msg = _("You can't save an item for later if you're "
                            "not logged in!")
                    flash_messages.error(msg)
                    return redirect(self.get_success_url())

        if save_for_later:
            # No need to call super if we're moving lines to the saved basket
            response = redirect(self.get_success_url())
        else:
            # Save changes to basket as per normal
            response = super().formset_valid(formset)

        # If AJAX submission, don't redirect but reload the basket content HTML
        if self.request.is_ajax():
            # Reload basket and apply offers again
            self.request.basket = get_model('basket', 'Basket').objects.get(
                id=self.request.basket.id)
            self.request.basket.strategy = self.request.strategy
            Applicator().apply(self.request.basket, self.request.user,
                               self.request)
            offers_after = self.request.basket.applied_offers()

            for level, msg in BasketMessageGenerator().get_messages(
                    self.request.basket, offers_before, offers_after, include_buttons=False):
                flash_messages.add_message(level, msg)

            # Reload formset - we have to remove the POST fields from the
            # kwargs as, if they are left in, the formset won't construct
            # correctly as there will be a state mismatch between the
            # management form and the database.
            kwargs = self.get_formset_kwargs()
            del kwargs['data']
            del kwargs['files']
            if 'queryset' in kwargs:
                del kwargs['queryset']
            formset = self.get_formset()(queryset=self.get_queryset(),
                                         **kwargs)
            ctx = self.get_context_data(formset=formset,
                                        basket=self.request.basket)
            return self.json_response(ctx, flash_messages)

        BasketMessageGenerator().apply_messages(self.request, offers_before)
    
        return response

    def get_context_data(self, **kwargs):
        context = super(BasketItemView, self).get_context_data(**kwargs)
        now = timezone.now()
        context['voucher_list'] = Voucher.objects.filter(start_datetime__lte=now, end_datetime__gte=now)
        try:
            context['applied_voucher_list'] = [voucher.code for voucher in self.request.basket.vouchers.all() if hasattr(self.request.basket, 'vouchers')]
        except Exception as e:
            pass  
        
        return context


class BasketItemOrderSummaryView(BasketView):
    """
    basket item detail
    """    
    template_name = 'basket/partials/basket_order_summary.html'

    def get_context_data(self, **kwargs):
        context = super(BasketItemOrderSummaryView, self).get_context_data(**kwargs)
        now = timezone.now()
        context['voucher_list'] = Voucher.objects.filter(start_datetime__lte=now, end_datetime__gte=now)
        
        try:
            context['applied_voucher_list'] = [voucher.code for voucher in self.request.basket.vouchers.all() if hasattr(self.request.basket, 'vouchers')]
        except Exception as e:
            pass  
        
        return context

class BasketItemOrderSummaryMobileView(BasketView):
    """
    basket item detail
    """    
    template_name = 'basket/partials/basket_order_summary_mobile.html'

    def get_context_data(self, **kwargs):
        context = super(BasketItemOrderSummaryMobileView, self).get_context_data(**kwargs)
        now = timezone.now()
        context['voucher_list'] = Voucher.objects.filter(start_datetime__lte=now, end_datetime__gte=now)
        
        try:
            context['applied_voucher_list'] = [voucher.code for voucher in self.request.basket.vouchers.all() if hasattr(self.request.basket, 'vouchers')]
        except Exception as e:
            pass  
        
        return context


