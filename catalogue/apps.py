# oscar imports
import oscar.apps.catalogue.apps as apps
from oscar.core.loading import get_class

#django imports
from django.conf.urls import url, include

class CatalogueConfig(apps.CatalogueConfig):
    name = 'catalogue'
   
    def ready(self):
        super().ready()
        self.detail_view = get_class('catalogue.views', 'ProductDetailsView')
        self.catalogue_view = get_class('catalogue.views', 'ProductListView')
        # self.homepage_view = get_class('catalogue.views', 'HomepageView')
        self.site_latest_product_view = get_class('catalogue.views', 'SiteLatestProductView')
        # self.aboutus_view = get_class('catalogue.views','AboutUsView')
        # self.contact_us_view = get_class('catalogue.views','ContactUsView')
        # self.privacy_policy_view = get_class('catalogue.views','PrivacyPolicyView')
        # self.terms_of_use_view = get_class('catalogue.views','TermsOfUseView')
        # self.return_policy_view = get_class('catalogue.views','ReturnPolicyView')
        # self.shipping_policy_view = get_class('catalogue.views','ShippingPolicyView')
        # self.faq_view = get_class('catalogue.views','FaqView')
        # self.blog_view = get_class('catalogue.views','BlogView')
        # self.blog_detail_view = get_class('catalogue.views','BlogDetailView')
        self.basket_item_detail = get_class('catalogue.views', 'BasketItemDetailView') 
        self.get_category_product_list = get_class('catalogue.views', 'CategoryProductListView')  
        self.dietician_detail = get_class('catalogue.views', 'DieticianDetailView')  
        self.product_list_filter_view = get_class('catalogue.views', 'ProductListFilterView')
        self.dietitian_advice_list_view = get_class('catalogue.views', 'DietitianAdviceListView')
        

    def get_urls(self):
        urls = []
        urls += [
            # url(r'^$', self.homepage_view.as_view(), name='index'),
            url(r'^product/$', self.catalogue_view.as_view(), name='product_list'),
            url(r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$',
                self.detail_view.as_view(), name='detail'),
            url(r'^category/(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/$',
                self.category_view.as_view(), name='category'),
            url(r'^latest_product/$', self.site_latest_product_view.as_view(), name='site_latest_product'),
            url(r'^ranges/(?P<slug>[\w-]+)/$',
                self.range_view.as_view(), name='range'),
            url(r'^basket-item-detail/$', self.basket_item_detail.as_view(), name='basket_item_detail'),
            url(r'^product-category-list', self.get_category_product_list.as_view(), name='product_category_list'),
            url(r'^dietician-detail', self.dietician_detail.as_view(), name='dietician-detail'),
            url(r'^product-list-filter$', self.product_list_filter_view.as_view(), name='product_list_filter'),
            url(r'^dietitian_advice_list$', self.dietitian_advice_list_view.as_view(), name='dietitian_advice_list'),
            url(r'^api/', include('catalogue.api.urls')),
        ]
        return self.post_process_urls(urls)