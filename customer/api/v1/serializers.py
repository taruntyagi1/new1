# python imports

# oscar imports
from unittest.util import _MAX_LENGTH
from oscar.core.loading import get_model

# django imports
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

# inner app imports
from canleath.validators import NAME_VALIDATOR

# third party imports
from rest_framework import serializers
from phonenumber_field.validators import validate_international_phonenumber

from oscarapi.utils.settings import overridable

User = get_user_model()
UserAddress = get_model('address', 'useraddress')
Country = get_model('address', 'country')
Voucher = get_model("voucher", "Voucher")
Range = get_model('offer', 'Range')


class SendOTPSerializer(serializers.Serializer):
    """
    Send Otp to requested Mobile Number
    """
    mobile_number = serializers.CharField(
        validators=[
            validate_international_phonenumber,
        ]
    )


class ValidateOtpSerializer(serializers.Serializer):
    """
    Validate otp Serializer
    """
    mobile_number = serializers.CharField(
        validators=[
            validate_international_phonenumber,
        ]
    )

    otp = serializers.CharField(max_length=6)    


class UserAddSerializer(serializers.ModelSerializer):
    """
    Sign up serializer
    """

    first_name = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'mobile_number',
            'gender',
            'dob',
            'profile_picture',
            'terms_and_conditions',
        )

        read_only_fields = (
            'id',
            'last_name',
            'gender',
            'dob',
            'profile_picture',
            'terms_and_conditions',
        )

    def validate_email(self, email):
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError('A user with this email is already exists')
        elif email:
            return email
        else:
            return None

    def validate_mobile_number(self, mobile_number):
        if mobile_number and User.objects.filter(mobile_number=mobile_number).exists():
            raise serializers.ValidationError('A user with this mobile is already exists')
        elif mobile_number:
            return mobile_number
        else:
            return None


class UserAddressSerializer(serializers.ModelSerializer):
    """
    serializer for validating user address field
    """

    # country_url = serializers.HyperlinkedRelatedField(
    #     view_name="country-detail", queryset=Country.objects, required=False,
    # )
    country_url = serializers.SerializerMethodField()

    class Meta:
        model = UserAddress
        fields = ['id',
            'user', 'title', 'first_name', 'last_name', 'email',
            'address_type', 'get_address_type_display',
            'line1', 'line2', 'line3', 'line4',
            'state', 'postcode',
            'phone_number', 'notes', 'country_url', 'get_country_id', 'alternate_mobile_number',
        ]

        read_only_fields = (
            'id',
            'country_url'
            'get_address_type_display'
            'get_country_id'
        )

    def get_country_url(self, obj):
        if obj.country:
            return reverse("country-detail", kwargs={'pk': obj.country.pk})
        return None

    def validate_email(self, email):
        if email:
            return email
        else:
            raise serializers.ValidationError('This field is required')

    def create(self, validated_data):
        local_country = Country.objects.filter(printable_name="India")
        user_address = UserAddress(**validated_data)
        user_address.country = local_country[0] if local_country.exists() else None
        user_address.save()
        return user_address


class CoupenCodeSerializer(serializers.ModelSerializer):
    """
    Sign up serializer
    """
    benefit_range = serializers.CharField(max_length=100)
    benefit_type = serializers.CharField(max_length=100)
    benefit_value = serializers.IntegerField()
    created_from = serializers.CharField(max_length=100)
    max_discount_value = serializers.FloatField(required=False)
    class Meta:
        model = Voucher

        fields =(
            "id",
            "name",
            "code",
            "start_datetime",
            "end_datetime",
            "usage", 
            "benefit_range",
            "benefit_type", 
            "benefit_value",
            "created_from",
            "max_discount_value"
        )

        read_only_fields = (
            'id',
        )

        
class CouponCodeUpdateSerializer(serializers.ModelSerializer):
    """
    Range serializer
    """
 
    benefit_value = serializers.IntegerField()

    class Meta:
        model = Voucher

        fields =(
            "id",
            "benefit_value"
        )

        read_only_fields = (
            'id',
        )


class RangeSerializer(serializers.ModelSerializer):
    """
    Range serializer
    """
 
   
    class Meta:
        model = Range

        fields =(
            "id",
            "name"
        )

        read_only_fields = (
            'id',
        )


class UserListSerializer(serializers.ModelSerializer):
    """
    user serializer
    """       

    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
            'mobile_number',
            'email',
        )