# python imports
import uuid

# django imports
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from django.conf import settings
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.views.generic import (
    TemplateView,
  
)
from django.utils import timezone

# oscar imports
from oscar.apps.checkout.views import (
    ShippingAddressView,
    PaymentDetailsView,
    UserAddressUpdateView,
    UserAddressDeleteView,
    ThankYouView,
    ShippingMethodView,
)
from address.models import UserAddress
from basket.utils import user_coupon_code_transaction

from checkout.models import UserTransaction
from customer.api.v1.serializers import Country
from order.models import Order
from shipping.repository import Repository

# third party imports
import razorpay

from voucher.models import Voucher

class CustomShippingMethodView(ShippingMethodView):
    """
    customized shipping method view
    """
    success_url = reverse_lazy('checkout:preview')
    template_name = 'checkout/shipping_methods.html'

    def get_available_shipping_methods(self):
        """
        Returns all applicable shipping method objects for a given basket.
        """
        # Shipping methods can depend on the user, the contents of the basket
        # and the shipping address (so we pass all these things to the
        # repository).  I haven't come across a scenario that doesn't fit this
        # system.
        return Repository().get_shipping_methods(
            basket=self.request.basket, user=self.request.user,
            shipping_addr=self.get_shipping_address(self.request.basket),
            request=self.request)


class GetCheckoutView(TemplateView):
    """
    checkout view
    """

    template_name = 'checkout/shipping_address.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GetCheckoutView, self).get_context_data(*args, **kwargs)
        context['voucher_list'] = Voucher.objects.all()
        if self.request.user.is_authenticated:
            context['addresses'] = UserAddress.objects.filter(user=self.request.user)
            context['orders'] =  self.request.basket.all_lines()
        context['country'] = Country.objects.all()
        return context     



class ShippingAddressListView(TemplateView):
    """
    shipping view
    """

    template_name = 'checkout/partials/shipping_address_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShippingAddressListView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context['addresses'] = UserAddress.objects.filter(user=self.request.user)
        return context     



class CustomShippingAddressView(ShippingAddressView):
    """
    customized shipping address view
    """

    template_name = 'checkout/shipping_address_old.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CustomShippingAddressView, self).get_context_data(*args, **kwargs)
        context['voucher_list'] = Voucher.objects.all()
        return context     


class CustomPaymentDetailsView(PaymentDetailsView):
    """
    Custom payment detail view
    """
    template_name = 'checkout/payment_details.html'
    template_name_preview = 'checkout/preview.html'

    # def handle_payment(self, order_number, total, **kwargs):
    #     """
    #     Handle any payment processing and record payment sources and events.

    #     This method is designed to be overridden within your project.  The
    #     default is to do nothing as payment is domain-specific.

    #     This method is responsible for handling payment and recording the
    #     payment sources (using the add_payment_source method) and payment
    #     events (using add_payment_event) so they can be
    #     linked to the order when it is saved later on.
    #     """
    #     user_transation = get_object_or_404(UserTransaction, id=self.request.POST.get('user_transaction_id'))
    #     user_transation.order_number = order_number
    #     user_transation.save()
    #     pass


class CustomUserAddressUpdateView(UserAddressUpdateView):
    """
    Custom payment detail view
    """

    template_name = 'checkout/user_address_form.html'


class CustomUserAddressDeleteView(UserAddressDeleteView):
    """
    user address delete view
    """

    template_name = 'checkout/user_address_delete.html'


class CustomThankYouView(ThankYouView):
    """
    custom order confirmation view
    """

    template_name = 'checkout/thank_you.html'
   
    def get_context_data(self, *args, **kwargs):
        
        ctx = super(CustomThankYouView, self).get_context_data(*args, **kwargs)
      
        order = ctx['object']
        # user_transaction = UserTransaction.objects.get(order_number=order.number)
        # user_transaction.order = order
        # user_transaction.save()
        # order.payment_done = True
        # order.save()
        # if order.basket.vouchers.first().created_from == "IF":
        #     user_coupon_code_transaction(order)
        return ctx


class PaymentCreateView(View):
    """
    Custom Payment Create View
    """

    template_name = 'checkout/payment_create.html'
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(PaymentCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        raise Http404('cant use get request')

    def post(self, request, *args, **kwargs):
        data = request.POST
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))
        order_currency = data.get('currency')
        order_total = float(data.get('amount'))
        # order_number = data.get('number')
        order_amount = float(data.get('amount'))*100
        data = {
            'amount': order_amount,
            'currency': order_currency,
            'payment_capture': 1,
        }
        data['notes'] = {
            'name': request.user.full_name,
            'email': request.user.email,
            'uid': uuid.uuid4().int
        }
        order = client.order.create(data=data)
        order_id = order['id']
        # order_data= request.session.pop('order_data')
        # order_number=order_data.get('order_number')
        # request.session['checkout_order_id'] = order_data.get('checkout_order_id')
        user_transaction = UserTransaction.objects.create(
            # order_number = order_number,
            amount=order_total,
            user=request.user,
            rz_order_id=order_id,
            status='C',
        )
        context = {
            'key': settings.RAZORPAY_KEY,
            'buttontext': 'Proceed To Pay',
            'order_id': order_id,
            'amount': order_amount,
            'currency': order_currency,
            'order_total': order_total,
            'user_transaction': user_transaction.id,
            # 'order_number' : user_transaction.order_number
        }
        request.session['user_transaction_id'] = user_transaction.id
        return render(request, self.template_name, context=context)


# depracated not using currently
class GetPaymentStatusView(View):
    template_name = 'checkout/payment_success.html'
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(GetPaymentStatusView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        raise Http404('cant use get request')

    def post(self, request):
       
        data = request.POST
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))
        try:
            client.utility.verify_payment_signature(request.POST)
        except:
            print('error')
            return HttpResponse(f'Fail')
        
        user_transaction_id = request.session.pop('user_transaction_id')
        # user_transaction_id = data.get('user_transaction_id')
        user_transaction = get_object_or_404(UserTransaction, id=user_transaction_id)
        user_transaction.rz_payment_id = data.get('razorpay_payment_id')
        user_transaction.razorpay_signature = data.get('razorpay_signature')
        user_transaction.status = 'P'
        user_transaction.save()
        # order_data= request.session.pop('order_data')
        # checkout_order_id=order_data.get('checkout_order_id')
        # order=Order.objects.get(number=user_transaction.order_number)
        context = {
            'user_transaction_id': user_transaction_id,
            'order_number':user_transaction.order_number,
            # 'checkout_order_id':order.id
        }
        return render(request, self.template_name, context=context)
