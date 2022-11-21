# django imports
from django.urls import path

# third party imports
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

# local imports
from .views import (
    CouponCodeAddApiView,
    CouponCodeUpdateApiView,
    GenerateOtpAPIView,
    RangeListAPIView,
    UserAddApiView,
    CustomerLoginWithoutOTPApiView,
    CustomerAddressApiViewSet,
    UserDetailView,
    ValidateOtpAPIView, 
    VerifyPaymentStatusApiView,
    UserListApiView,
)

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'^customer-address', CustomerAddressApiViewSet, basename='customer_address')

urlpatterns = [
    path('generate-otp', GenerateOtpAPIView.as_view(), name='generate_otp'),
    path('validate-otp', ValidateOtpAPIView.as_view(), name='validate_otp'),
    path('user-add', UserAddApiView.as_view(), name='user_add_api'),
    path('customer-login', CustomerLoginWithoutOTPApiView.as_view(), name='customer_login_api'),
    path("users/<int:pk>/", UserDetailView.as_view(), name="custom_user-detail"),
    path('coupon-code-add', CouponCodeAddApiView.as_view(), name='user_add_api'),
    path('coupon-code-update/<str:code>/', CouponCodeUpdateApiView.as_view(), name='coupon_code_update_api'),
    path('range-list', RangeListAPIView.as_view(), name='range_list_api'),
    path('verify-payment-status', VerifyPaymentStatusApiView.as_view(), name='verify_payment_status'),
    path('user-list-api', UserListApiView.as_view(), name='user_list_api'),
  
]

# adding router urls
urlpatterns += router.urls

# Add Multiple Format Support
urlpatterns = format_suffix_patterns(urlpatterns)