# django imports
from django.urls import path, include

# third party imports
from rest_framework.urlpatterns import (
    format_suffix_patterns,
)
from rest_framework import routers

# inner app imports
from .views import (
    DietitionsAndNutritionistsApiViewSet,
    ProductApiViewSet,
    CategoryApiViewSet,
    BannerImageApiViewSet,
    BasketView,
    BasketList,
    BasketDetail,
    LineList,
    BasketLineDetail,
    AddProductView,
    CheckoutView,
    OrderList,
    OrderDetail,
    OrderLineList,
    OrderLineDetail,
    OrderUpdateApiView,
    AddVoucherView,
    QuestionaireCreateApiView,
    ValidateCheckoutView,
    VoucherRemoveApiView,
    ShippingMethodView,
    
)

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'^category', CategoryApiViewSet, basename='category_api')
# router.register(r'^product', ProductApiViewSet, basename='product_api')
router.register(r'^banner', BannerImageApiViewSet, basename='banner_api')
router.register(r'^dietitions_and_nutritionists', DietitionsAndNutritionistsApiViewSet, basename='dietitions_and_nutritionists')
product_detail = ProductApiViewSet.as_view({
    'get': 'retrieve',
})

product_list = ProductApiViewSet.as_view({
    'get': 'list',
})

urlpatterns = [ 
    path("product/", product_list, name="product_list_api"),
    path("product/<int:pk>/", product_detail, name="product_detail"),
    path("basket/", BasketView.as_view(), name="api-catalogue-basket"),
    path("baskets/", BasketList.as_view(), name="basket-list"),
    path("baskets/<int:pk>/", BasketDetail.as_view(), name="basket-detail"),
    path("baskets/<int:pk>/lines/", LineList.as_view(), name="basket-lines-list"),
    path("baskets/<int:basket_pk>/lines/<int:pk>/", BasketLineDetail.as_view(), name="basket-line-detail",),
    path("basket/add-product/", AddProductView.as_view(), name="basket-add-product"),
    path("validate-checkout/", ValidateCheckoutView.as_view(), name="api-validate-checkout"),
    path("checkout/", CheckoutView.as_view(), name="api-checkout"),
    path("orders", OrderList.as_view(), name="order_list_api"),
    path("orders/<int:pk>/", OrderDetail.as_view(), name="order_detail_api"),
    path("orders/<int:pk>/update",OrderUpdateApiView.as_view(), name="order_update_api"),
    path("orders/<int:pk>/lines/", OrderLineList.as_view(), name="order_lines_list_api"),
    path("orderlines/<int:pk>/", OrderLineDetail.as_view(), name="order_lines_detail_api"),
    path("basket/add-voucher/", AddVoucherView.as_view(), name="basket_add_voucher_api"),
    path("basket/remove-voucher/", VoucherRemoveApiView.as_view(), name="basket_remove_voucher_api"),
    path("basket/shipping-methods/", ShippingMethodView.as_view(), name="basket_shipping_method_api"),
    path("questionaire-create", QuestionaireCreateApiView.as_view(), name="questionaire_create_api"),
]


# adding router urls
urlpatterns += router.urls

# Add Multiple Format Support
urlpatterns = format_suffix_patterns(urlpatterns)