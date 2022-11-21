# oscar imports
import oscar.apps.customer.apps as apps
from oscar.core.loading import get_class

# django imports
from django.conf.urls import url, include
from django.urls import reverse_lazy

class CustomerConfig(apps.CustomerConfig):
    name = 'customer'

    def ready(self):
        from django.contrib.auth.forms import SetPasswordForm

        super(CustomerConfig, self).ready()
        self.login_view = get_class('customer.views', 'LoginView')
        self.register_view = get_class('customer.views', 'RegistrationView')
        self.profile_view = get_class('customer.views', 'CustomProfileView')
        self.change_password_view = get_class('customer.views', 'CustomChangePasswordView')
        self.profile_update_view = get_class('customer.views', 'CustomProfileUpdateView')
        self.profile_delete_view = get_class('customer.views', 'CustomProfileDeleteView')
        self.order_history_view = get_class('customer.views', 'CustomOrderHistoryView')
        self.order_detail_view = get_class('customer.views', 'CustomOrderDetailView')
        self.address_list_view = get_class('customer.views', 'CustomAddressListView')
        self.address_create_view = get_class('customer.views', 'CustomAddressCreateView')
        self.address_update_view = get_class('customer.views', 'CustomAddressUpdateView')
        self.address_delete_view = get_class('customer.views', 'CustomAddressDeleteView')
        self.email_list_view = get_class('customer.views', 'CustomEmailHistoryView')
        self.email_detail_view = get_class('customer.views', 'CustomEmailDetailView')
        self.alert_list_view = get_class('customer.views', 'CustomProductAlertListView')
        self.alert_create_view = get_class('customer.views', 'CustomProductAlertCreateView')
        # self.notification_inbox_view = get_class('customer.views', 'CustomInboxView')
        # self.notification_archive_view = get_class('customer.views', 'CustomArchiveView')
        # self.notification_detail_view = get_class('customer.views', 'CustomDetailView')
        self.wishlists_list_view = get_class('customer.views', 'CustomWishListListView')
        self.wishlists_detail_view = get_class('customer.views', 'CustomWishListDetailView')
        self.wishlists_create_view = get_class('customer.views', 'CustomWishListCreateView')
        self.wishlists_delete_view = get_class('customer.views', 'CustomWishListDeleteView')
        self.wishlists_update_view = get_class('customer.views', 'CustomWishListUpdateView')
        self.wishlists_remove_product_view = get_class('customer.views', 'CustomWishListRemoveProduct')
        self.password_reset_form = get_class('customer.forms', 'PasswordResetForm')
        self.set_password_form = SetPasswordForm
        self.admin_login = get_class('customer.views', 'AdminLoginView')


    def get_urls(self):
        from django.contrib.auth import views as auth_views
        from oscar.views.decorators import login_forbidden
        urls = super(CustomerConfig, self).get_urls()
        urls += [
            url(r'^password-reset/$',
                login_forbidden(
                    auth_views.PasswordResetView.as_view(
                        form_class=self.password_reset_form,
                        success_url=reverse_lazy('customer:password-reset-done'),
                        template_name='customer/registration/password_reset_form.html'
                    )
                ),
                name='password-reset'),
            url(r'^password-reset/done/$',
                login_forbidden(auth_views.PasswordResetDoneView.as_view(
                    template_name='customer/registration/password_reset_done.html'
                )),
                name='password-reset-done'),
            url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                login_forbidden(
                    auth_views.PasswordResetConfirmView.as_view(
                        form_class=self.set_password_form,
                        success_url=reverse_lazy('customer:password-reset-complete'),
                        template_name='customer/registration/password_reset_confirm.html'
                    )
                ),
                name='password-reset-confirm'),
            url(r'^password-reset/complete/$',
                login_forbidden(auth_views.PasswordResetCompleteView.as_view(
                    template_name='customer/registration/password_reset_complete.html'
                )),
                name='password-reset-complete'),
            url(r'^admin-login/$', self.admin_login.as_view(), name='admin_login'),
            url(r'^api/', include('customer.api.urls')),
        ]
        return urls
