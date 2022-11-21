# oscar imports
import oscar.apps.checkout.apps as apps
from oscar.core.loading import get_class
# django imports
from django.conf.urls import url

class CheckoutConfig(apps.CheckoutConfig):
    name = 'checkout'

    def ready(self):
        super(CheckoutConfig, self).ready()
        self.shipping_method_view = get_class('checkout.views', 'CustomShippingMethodView')
        self.shipping_address_view = get_class('checkout.views', 'CustomShippingAddressView')
        self.payment_details_view = get_class('checkout.views', 'CustomPaymentDetailsView')
        self.user_address_update_view = get_class('checkout.views', 'CustomUserAddressUpdateView')
        self.user_address_delete_view = get_class('checkout.views', 'CustomUserAddressDeleteView')
        self.thankyou_view = get_class('checkout.views', 'CustomThankYouView')
        self.payment_create_view = get_class('checkout.views', 'PaymentCreateView')
        self.payment_status_view = get_class('checkout.views', 'GetPaymentStatusView')
        self.checkout_view = get_class('checkout.views', 'GetCheckoutView')
        self.shipping_address_list_view = get_class('checkout.views', 'ShippingAddressListView')

    def get_urls(self):
        from django.contrib.auth import views as auth_views
        from oscar.views.decorators import login_forbidden
        urls = super(CheckoutConfig, self).get_urls()
        urls += [
            url(r'^checkout/$', self.checkout_view.as_view(), name='checkout'),
            url(r'^payment-create/$', self.payment_create_view.as_view(), name='payment_create'),
            url(r'^payment-status/$', self.payment_status_view.as_view(), name='payment_status'),
            url(r'^shipping-address/list$', self.shipping_address_list_view.as_view(), name='shipping_address_list'),
        ]
        return urls