# oscar imports
import oscar.apps.basket.apps as apps
from oscar.core.loading import get_class
from django.conf.urls import url

class BasketConfig(apps.BasketConfig):
    name = 'basket'

    def ready(self):
        super(BasketConfig, self).ready()
        self.summary_view = get_class('basket.views', 'CustomBasketView')
        self.add_voucher_view = get_class('basket.views', 'VoucherAddView')
        self.basket_item_view = get_class('basket.views', 'BasketItemView')
        self.basket_item_order_summary_view = get_class('basket.views', 'BasketItemOrderSummaryView')
        self.basket_item_order_summary_mobile_view = get_class('basket.views', 'BasketItemOrderSummaryMobileView')
        
    
    def get_urls(self):
        urls = []
        urls += [
            url(r'^$', self.summary_view.as_view(), name='summary'),
            url(r'^vouchers/add/$', self.add_voucher_view.as_view(),
                    name='vouchers-add'),
            url(r'^vouchers/(?P<pk>\d+)/remove/$',
                self.remove_voucher_view.as_view(), name='vouchers-remove'),
            url(r'^basket_items$', self.basket_item_view.as_view(), name='basket_items'),
            url(r'^basket_item_order_summary$', self.basket_item_order_summary_view.as_view(), name='basket_item_order_summary_view'),
            url(r'^basket_item_order_summary_mobile$', self.basket_item_order_summary_mobile_view.as_view(), name='basket_item_order_summary_mobile'),
        ]
        return self.post_process_urls(urls)
    
