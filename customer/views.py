# django imports
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _

# oscar imports
from oscar.apps.customer.views import (
    AccountAuthView,
    ProfileView,
    ChangePasswordView,
    ProfileUpdateView,
    ProfileDeleteView,
    OrderHistoryView,
    OrderDetailView,
    AddressListView,
    AddressCreateView,
    AddressUpdateView,
    AddressDeleteView,
    EmailHistoryView,
    EmailDetailView,
)

from oscar.apps.customer.alerts.views import (
    ProductAlertListView,
    ProductAlertCreateView,
)
from oscar.core.loading import get_class

# from oscar.apps.customer.notifications.views import (
#     NotificationListView,
#     DetailView,
# )

from oscar.apps.customer.wishlists.views import (
    WishListListView,
    WishListDetailView,
    WishListCreateView,
    WishListUpdateView,
    WishListDeleteView,
    WishListRemoveProduct,
)

from oscar.core.utils import redirect_to_referrer, safe_referrer

from canleath.messages import SUCCESS_MESSAGES

# local imports
from .forms import (
    CustomEmailUserCreationForm,
    CustomAuthenticationForm,
    ProfileForm,
)
from .mixins import CustomRegisterUserMixin

UserAddressForm = get_class('address.forms', 'UserAddressForm')

class LoginView(AccountAuthView):
    """
    A view for login
    """

    template_name = 'customer/registration/login.html'
    login_form_class = CustomAuthenticationForm


class AdminLoginView(AccountAuthView):
    """
    A view for login
    """

    template_name = 'customer/registration/admin_login.html'
    login_form_class = CustomAuthenticationForm


class RegistrationView(CustomRegisterUserMixin, AccountAuthView):
    """
    A view for login
    """

    template_name = 'customer/registration/register.html'
    registration_form_class = CustomEmailUserCreationForm


class CustomProfileView(ProfileView):
    """
    Customized Profile View
    """

    template_name = 'customer/profile/profile.html'


class CustomChangePasswordView(ChangePasswordView):
    """
    Customized Change Password View
    """

    template_name = 'customer/profile/change_password_form.html'


class CustomProfileUpdateView(ProfileUpdateView):
    """
    Customized Profile Update View
    """

    form_class = ProfileForm
    template_name = 'customer/profile/profile_form.html'


class CustomProfileDeleteView(ProfileDeleteView):
    """
    Customized profile delete view
    """

    template_name = 'customer/profile/profile_delete.html'


class CustomOrderHistoryView(OrderHistoryView):
    """
    Customized order history view
    """

    template_name = 'customer/order/order_list.html'


class CustomOrderDetailView(OrderDetailView):
    """
    Customized order detail view
    """

    def get_template_names(self):
        return ["customer/order/order_detail.html"]


class CustomAddressListView(AddressListView):
    """
    Customized address list view
    """

    template_name = 'customer/address/address_list.html'


class CustomAddressCreateView(AddressCreateView):
    """
    Customized address create view
    """
    form_class = UserAddressForm
    template_name = 'customer/address/address_form.html'

    def get_success_url(self):
        messages.success(self.request, SUCCESS_MESSAGES['ADDRESS_CREATED'])
        return (reverse_lazy('customer:address-list'))


class CustomAddressUpdateView(AddressUpdateView):
    """
    Customized address update view
    """
    form_class = UserAddressForm
    template_name = 'customer/address/address_form.html'

    def get_success_url(self):
        messages.success(self.request, SUCCESS_MESSAGES['ADDRESS_UPDATE'])
        return (reverse_lazy('customer:address-list'))



class CustomAddressDeleteView(AddressDeleteView):
    """
    Customized address delete view
    """

    template_name = 'customer/address/address_delete.html'

    def get_success_url(self):
        messages.success(self.request, SUCCESS_MESSAGES['ADDRESS_DELETE'])
        return (reverse_lazy('customer:address-list'))



class CustomEmailHistoryView(EmailHistoryView):
    """
    Customized email list view
    """

    template_name = 'customer/email/email_list.html'


class CustomEmailDetailView(EmailDetailView):
    """
    Customized email detail view
    """

    template_name = 'customer/email/email_detail.html'


class CustomProductAlertListView(ProductAlertListView):
    """
    Customized product alert list view
    """

    template_name = 'customer/alerts/alert_list.html'


class CustomProductAlertCreateView(ProductAlertCreateView):
    """
    Customized product alert create view
    """

    template_name = 'customer/alerts/form.html'


# class CustomNotificationListView(NotificationListView):
#     """
#     Customized notification list view
#     """
#
#     template_name = 'customer/notifications/list.html'


# class CustomInboxView(CustomNotificationListView):
#     """
#     Customized inbox view
#     """
#     list_type = 'inbox'
#
#     def get_queryset(self):
#         return self.model._default_manager.filter(
#             recipient=self.request.user,
#             location=self.model.INBOX)


# class CustomArchiveView(CustomNotificationListView):
#     """
#     Customized archive view
#     """
#
#     list_type = 'archive'
#
#     def get_queryset(self):
#         return self.model._default_manager.filter(
#             recipient=self.request.user,
#             location=self.model.ARCHIVE)


# class CustomDetailView(DetailView):
#     """
#     Customized detail view
#     """
#
#     template_name = 'customer/notifications/detail.html'


class CustomWishListListView(WishListListView):
    """
    Customized wishlist list view
    """

    template_name = 'customer/wishlists/wishlists_list.html'


class CustomWishListDetailView(WishListDetailView):
    """
    Customized wishlist detail view
    """

    template_name = 'customer/wishlists/wishlists_detail.html'


class CustomWishListCreateView(WishListCreateView):
    """
    Customized wishlist create view
    """

    template_name = 'customer/wishlists/wishlists_form.html'


class CustomWishListUpdateView(WishListUpdateView):
    """
    Customized wishlist update view
    """

    template_name = 'customer/wishlists/wishlists_form.html'


class CustomWishListDeleteView(WishListDeleteView):
    """
    Customized wishlist update view
    """

    template_name = 'customer/wishlists/wishlists_delete.html'


class CustomWishListRemoveProduct(WishListRemoveProduct):
    """
    Customized wishlist product remove view
    """

    def get_success_url(self):
        msg = _("'%(title)s' was removed from your '%(name)s' wish list") % {
            'title': self.line.get_title(),
            'name': self.wishlist.name}
        messages.success(self.request, msg)

        # We post directly to this view on product pages; and should send the
        # user back there if that was the case
        referrer = safe_referrer(self.request, '')
        if (referrer and self.product
                and self.product.get_absolute_url() in referrer):
            return referrer
        elif referrer and self.product:
            return referrer
        else:
            return reverse(
                'customer:wishlists-detail', kwargs={'key': self.wishlist.key})