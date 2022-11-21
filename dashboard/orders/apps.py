import oscar.apps.dashboard.orders.apps as apps
from django.conf.urls import url


class OrdersDashboardConfig(apps.OrdersDashboardConfig):
    name = 'dashboard.orders'
    def ready(self):
        super(OrdersDashboardConfig, self).ready()
        from .views import (
            CustomizedOrderDetailView
        )
        self.order_detail_view = CustomizedOrderDetailView
        
    def get_urls(self):
        urls = super(OrdersDashboardConfig, self).get_urls()
        urls += [
            url(r'^(?P<number>[-\w]+)/$',
                self.order_detail_view.as_view(), name='order-detail'),
        ]
        return self.post_process_urls(urls)