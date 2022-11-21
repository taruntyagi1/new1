# oscar imports
import oscar.apps.dashboard.vouchers.apps as apps
from django.conf.urls import url

class VouchersDashboardConfig(apps.VouchersDashboardConfig):
    name = 'dashboard.vouchers'
    
    def ready(self):
        super(VouchersDashboardConfig, self).ready()
        from .views import (
            VoucherCreateView,
            VoucherListView,
            VoucherDetailView,
            VoucherUpdateView
            
        )
        self.create_view = VoucherCreateView
        self.list_view = VoucherListView
        self.stats_view = VoucherDetailView
        self.update_view = VoucherUpdateView
       
    def get_urls(self):
        urls = super(VouchersDashboardConfig, self).get_urls()
        urls += [
            url(r'^create/$', self.create_view.as_view(),
                name='voucher-create'),
            url(r'^$', self.list_view.as_view(), name='voucher-list'),

            url(r'^stats/(?P<pk>\d+)/$', self.stats_view.as_view(),
                name='voucher-stats'),

             url(r'^update/(?P<pk>\d+)/$', self.update_view.as_view(),
                name='voucher-update'),

        ]
        return self.post_process_urls(urls)