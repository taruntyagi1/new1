# oscar imports

from django.shortcuts import get_object_or_404
from oscar.core.loading import get_model
# django imports
from oscar.apps.voucher.utils import get_offer_name
from django.contrib.auth import (
    get_user_model,
    authenticate,
    login
)
from django.db.models import Q
from accounts.backends import MobileOTPAuthenticationBackEnd
from django.conf import settings

# inner app imports
from accounts.models import UserOTP
from canleath.utils import generete_auth_token_key
from canleath.messages import VALIDATION_ERROR_MESSAGES
from catalogue.models import Category
from checkout.models import UserTransaction
from catalogue.api.v1.pagination import ObjectPagination2x

#local imports
from .serializers import (
    CoupenCodeSerializer,
    CouponCodeUpdateSerializer,
    RangeSerializer,
    SendOTPSerializer,
    UserAddSerializer,
    UserAddressSerializer,
    ValidateOtpSerializer,
    UserListSerializer,
)

# third party imports
from rest_framework import generics
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import (
    mixins,
    viewsets,
    permissions,
)
import razorpay

Voucher = get_model("voucher", "Voucher")
ConditionalOffer = get_model('offer', 'ConditionalOffer')
Benefit = get_model('offer', 'Benefit')
Condition = get_model('offer', 'Condition')
User = get_user_model()
UserAddress = get_model('address', 'useraddress')
Range = get_model('offer', 'Range')

class GenerateOtpAPIView(GenericAPIView):
    """Generate Otp Api view

        Url: accounts/api/v1/generate-otp.json
        Name: generate_otp
        Method: POST
        Params: None
        Body : {
            'mobile_number' : mobile_number
        }
        Returns: success_data, Status, error_message

        Example: {
            'mobile_number' : mobile_number
        }
    """

    serializer_class = SendOTPSerializer

    def post(self, request, format=None):
        """
        generate otp
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile_number = serializer.validated_data.get('mobile_number')
        otp = UserOTP.objects.filter(mobile_number=mobile_number)
        if otp:
            otp = UserOTP.objects.filter(mobile_number=mobile_number).last()
        else:
            otp = UserOTP.objects.create(mobile_number=mobile_number)
        if self.request.data.get('purpose') == 'signup':
            if User.objects.filter(mobile_number=mobile_number).count() > 0:
                return Response({'status': False, 'text': 'A User With this Mobile Number Already Exist'}, status=status.HTTP_200_OK)
            otp.send_otp(UserOTP.MOBILE_VERIFICATION)
        else:
            user_obj = User.objects.filter(mobile_number=mobile_number).first()
            if hasattr(user_obj, 'is_superuser') and user_obj.is_superuser:
                otp.send_otp(UserOTP.LOGIN_VERIFICATION)
                otp.user = user_obj
                otp.save()
            elif user_obj:
                otp.send_otp(UserOTP.LOGIN_VERIFICATION)
            else:
                return Response({'status': False, 'text': 'There is no account with this mobile number'}, status=status.HTTP_200_OK)
        return Response({'otp':otp.password, 'status': True, 'text': 'OTP Sent to your mobile number'}, status=status.HTTP_200_OK)


class ValidateOtpAPIView(generics.GenericAPIView):
    """
    Trainee login api view it will validate the otp and authenticate user

    Url: accounts/api/v1/validate-otp.json
    Name: validate_otp
    Method: POST
    Params: None
    Body : {
        'mobile_number' : mobile_number,
        'otp':otp
    }
    Returns: success_data, Status, error_message
    Example: {
        'mobile_number' : mobile_number,
        'otp':otp
    }
    """
    serializer_class = ValidateOtpSerializer

    def post(self, request, format=None):
        """
        Authenticate user and return token in response
        """
        # import ipdb;ipdb.set_trace()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile_number = serializer.validated_data.get('mobile_number')
        otp = serializer.validated_data.get('otp')

        user_obj = User.objects.filter(mobile_number=mobile_number).first()
        otp_user = UserOTP.objects.filter(mobile_number=mobile_number)

        # if user_obj not mapped with otp_user than map it
        if otp_user.exists() and user_obj and not hasattr(user_obj, 'otp'):
            otp_user_obj = otp_user.order_by('-id').last()
            otp_user_obj.user = user_obj
            otp_user_obj.save()

        user = authenticate(mobile_number=mobile_number, otp=otp, strict_login_with_otp = True)  # authenticate user

        if user and user.is_active:
            user.is_mobile_number_verified=True
            user.save()
            data = UserAddSerializer(user).data
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # data.update(auth_key=user.get_auth_token())
            
            return Response({"status":True}, status=status.HTTP_200_OK)
        return Response({'detail': VALIDATION_ERROR_MESSAGES['INVALID_OTP']}, status=status.HTTP_401_UNAUTHORIZED)


class UserAddApiView(GenericAPIView):
    """
    User Add Api view

            Url: "http://if.sudofire.com/accounts/api/v1/user-add"
            Name: user_add
            Method: POST
            Params: None
            Body : {
                'first_name' : first_name
                'last_name' : last_name
                'mobile_number' : mobile_number
                'email' : email
                'gender' : gender
                'profile_picture' : profile_picture
                'terms_and_conditions' : terms_and_conditions
            }
            Returns: Status, error_message
    """

    serializer_class = UserAddSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           
            first_name = serializer.validated_data.get('first_name')
            # last_name = serializer.validated_data.get('last_name')
            email = serializer.validated_data.get('email')
            mobile_number = serializer.validated_data.get('mobile_number')
            # gender = serializer.validated_data.get('gender')
            # dob = serializer.validated_data.get('dob')

            user_obj = User.objects.create(
                
                # last_name=last_name,
                email=email,
                mobile_number=mobile_number,
                # gender=gender,
                # dob=dob,
            )
            if first_name or email:
                if first_name:
                    user_obj.first_name=first_name
                if email:
                    user_obj.email=email 
                user_obj.save()       

            # user_otp, created = UserOTP.objects.get_or_create(
            #     user=user_obj,
            #     password=get_user_model().objects.make_random_password(length=6, allowed_chars='0123456789'),
            #     mobile_number=mobile_number,
            #     purpose='LO'
            # )
            user_otp_list = UserOTP.objects.filter(Q(user=user_obj)|Q(mobile_number=mobile_number))
            if user_otp_list.exists():
                user_otp = user_otp_list.first()
                user_otp.mobile_number = mobile_number
                user_otp.purpose='LO'
                if not user_otp.user:
                    user_otp.user = user_obj
                user_otp.save()
            else:
                user_otp = UserOTP.objects.create(user=user_obj, mobile_number=mobile_number, purpose='LO')
            user_otp.send_otp(purpose=user_otp.purpose)
            return Response({'status': True,}, status=status.HTTP_201_CREATED)

        return Response({'status': False}, status=status.HTTP_400_BAD_REQUEST)


class CustomerLoginWithoutOTPApiView(GenericAPIView):
    """
    User login api view it will validate authenticate user

    Url: accounts/api/v1/customer-login.json
    Name: Customer Login
    Method: POST
    Params: None
    Body : {
        'mobile_number' : mobile_number,
    }
    Returns: success_data, Status, error_message
    Example: {
        'mobile_number' : mobile_number,
    }
    """

    serializer_class = SendOTPSerializer

    def post(self, request, format=None):
        """
        Authenticate user and return token in response
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile_number = serializer.validated_data.get('mobile_number')

        user = authenticate(mobile_number=mobile_number,)  # authenticate user

        if user and user.is_active:
            key = generete_auth_token_key()
            if hasattr(user, 'auth_token'):
                Token.objects.filter(user=user).update(key=key)
            else:
                Token.objects.create(user=user, key=key)
            data = UserAddSerializer(instance=user).data
            data.update(auth_key=key)
            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': VALIDATION_ERROR_MESSAGES['UNREGISTERED_MOBILE']}, status=status.HTTP_401_UNAUTHORIZED)


class CustomerAddressApiViewSet(viewsets.GenericViewSet,
                                mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.ListModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.UpdateModelMixin):
    """
    Api View for add and edit User Address
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserAddressSerializer

    def perform_create(self, serializer):
        user_obj = self.request.user
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        email = serializer.validated_data.get('email')
        if not user_obj.first_name and not user_obj.email and not User.objects.filter(email=email).exists():
            user_obj.first_name = first_name
            user_obj.last_name = last_name
            user_obj.email = email
            user_obj.save()
        serializer.save()

    def perform_update(self, serializer):
        user_obj = self.request.user
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        email = serializer.validated_data.get('email')
        if not user_obj.first_name and not user_obj.email and not User.objects.filter(email=email).exists():
            user_obj.first_name = first_name
            user_obj.last_name = last_name
            user_obj.email = email
            user_obj.save()
        serializer.save()    

    def get_queryset(self):
        if self.request.user.is_authenticated and hasattr(self.request.user, 'addresses'):
            queryset = UserAddress.objects.filter(user=self.request.user)
        elif self.request.GET.get('user_id', None):
            user_id = self.request.GET.get('user_id')
            queryset = UserAddress.objects.filter(user__id=user_id)
        else:
            queryset = UserAddress.objects.none()
        return queryset


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserAddSerializer
    permission_classes = (permissions.IsAuthenticated,)



class CouponCodeAddApiView(GenericAPIView):
    
    serializer_class = CoupenCodeSerializer
    def post(self, request, *args, **kwargs):
       
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            benefit_range = serializer.validated_data.get('benefit_range')
            name = serializer.validated_data.get('name')
            code = serializer.validated_data.get('code')
            start_datetime = serializer.validated_data.get('start_datetime')
            end_datetime = serializer.validated_data.get('end_datetime')
            usage = serializer.validated_data.get('usage')
            benefit_type = serializer.validated_data.get('benefit_type')
            benefit_value = serializer.validated_data.get('benefit_value')
            created_from = serializer.validated_data.get('created_from')
            benefit_range = Range.objects.get(name=benefit_range)
            max_discount_value = serializer.validated_data.get('max_discount_value')
            condition = Condition.objects.create(
                range=benefit_range,
                type=Condition.COUNT,
                value=1
            )

            benefit = Benefit.objects.create(
                range=benefit_range,
                type=benefit_type,
                value=benefit_value
            )
            
            offer = ConditionalOffer.objects.create(
                name=get_offer_name(name),
                offer_type=ConditionalOffer.VOUCHER,
                benefit=benefit,
                condition=condition,
                exclusive=True,
            )
            voucher = Voucher.objects.create(
                name=name,
                code=code,
                usage=usage,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                created_from=created_from,
                max_discount_value=max_discount_value
            )
            voucher.offers.add(offer)
                

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'Error': "Coupen code invalid"}, status=status.HTTP_400_BAD_REQUEST)


class CouponCodeUpdateApiView(generics.UpdateAPIView):
    
    serializer_class = CouponCodeUpdateSerializer

    def get_queryset(self):
            queryset = Voucher.objects.all()
            return queryset
    
    def get_object(self, **kwargs):
        return get_object_or_404(Voucher, code=self.kwargs.get('code'))

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            benefit_value = serializer.validated_data.get('benefit_value')
            voucher = serializer.save()
            offer = voucher.offers.all()[0]
            benefit = offer.benefit
            benefit.value = benefit_value
            benefit.save()
            
            data = {'message': benefit.value,}
            
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class RangeListAPIView(generics.ListAPIView):
    queryset = Range.objects.all()
    serializer_class = RangeSerializer
    

class VerifyPaymentStatusApiView(APIView):
    """
    custom paymemt verification view
    """

    def post(self, request, *args, **kwargs):
        data = self.request.data
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))
        try:
            client.utility.verify_payment_signature(data)
        except:
            print('error')
            return Response({'payment_status': False}, status=status.HTTP_200_OK)
        user_transaction_id = request.session.pop('user_transaction_id')
        user_transaction = get_object_or_404(UserTransaction, id=user_transaction_id)
        user_transaction.rz_payment_id = data.get('razorpay_payment_id'),
        user_transaction.razorpay_signature = data.get('razorpay_signature'),
        user_transaction.status = 'P'
        user_transaction.save()
        data = {
            'payment_status': True,
            'user_transaction_id': user_transaction.id,
        }    
        return Response(data=data, status=status.HTTP_200_OK)


class UserListApiView(ListAPIView):
    """
    custom user list view
    """        
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (permissions.IsAdminUser,)
    pagination_class = ObjectPagination2x

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)
        if self.request.GET.get('q', None):
            query = self.request.GET.get('q')
            queryset = queryset.filter(
                Q(first_name__icontains=query)
                |Q(last_name__icontains=query)
                |Q(email__icontains=query)
                |Q(mobile_number__icontains=query)
            )
        return queryset
