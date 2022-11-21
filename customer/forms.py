# django imports
from django.utils.http import is_safe_url
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

# oscar imports
from oscar.apps.customer import forms as base_forms
from oscar.core.loading import get_class, get_model, get_profile_class
from oscar.apps.customer.utils import get_password_reset_url, normalise_email
from oscar.core.compat import (
    existing_user_fields, get_user_model)

# inner app imports
from accounts.models import UserOTP
from canleath.messages import VALIDATION_ERROR_MESSAGES
from canleath.utils import BootstrapClearableFileInput, get_first_and_last_name
from canleath.validators import NAME_VALIDATOR

# third party imports
from phonenumber_field.formfields import PhoneNumberField


User = get_user_model()

class CustomEmailUserCreationForm(base_forms.EmailUserCreationForm):
    """
    customized user registration form
    """
    name = forms.CharField(max_length=200, validators=[NAME_VALIDATOR])
    otp = forms.CharField(label='OTP', max_length=6, required=True)

    class Meta(base_forms.EmailUserCreationForm.Meta):
        fields = (
            'name',
            'email',
            'mobile_number',
            'terms_and_conditions',
        )

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['mobile_number'].initial = '+91'
        self.fields['name'].widget.attrs["class"] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = "Enter Full Name"
        self.fields['mobile_number'].widget.attrs['placeholder'] = self.fields['mobile_number'].label
        self.fields['email'].widget.attrs["class"] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label
        self.fields['mobile_number'].widget.attrs["class"] = 'form-control'
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # self.fields['otp'].widget.attrs["class"] = 'form-control'
        # self.fields['otp'].widget.attrs['placeholder'] = 'Otp'

    def clean(self):
        """Validate cleaned data"""
        cleaned_data = super(self.__class__, self).clean()
        error_dict = {}

        # if cleaned_data.get('password1') or cleaned_data.get('password2'):
        #     if not (cleaned_data.get('password1') == cleaned_data.get('password2')):
        #         error_dict['password2'] = "Passwords don't match"

        otp = cleaned_data.get('otp')
        mobile_number = cleaned_data.get('mobile_number')
        try:
            otp_user = UserOTP.objects.get(mobile_number=mobile_number)
            if not otp_user.validate_otp(otp, UserOTP.MOBILE_VERIFICATION):
                error_dict['otp'] = 'OTP Is not Valid'
        except:
            error_dict['otp'] = 'OTP Is not Valid'

        if error_dict:
            raise forms.ValidationError(error_dict)

        return cleaned_data

    def save(self, commit=True):
        user = super(self.__class__, self).save(commit=False)
        # user.set_password(self.cleaned_data["password1"])
        first_name, last_name = get_first_and_last_name(self.cleaned_data.get('name'))
        user.first_name = first_name
        user.last_name = last_name
        mobile_number = self.cleaned_data["mobile_number"]
        otp = UserOTP.objects.filter(mobile_number=mobile_number)[0]
        if commit:
            user.save()
            otp.user = user
            otp.save()
        return user


class CustomAuthenticationForm(base_forms.EmailAuthenticationForm):
    """
    customized authentication form
    """

    username = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': 'Mobile Number', 'class': 'form-control'}),
        initial="+91",
        max_length=13
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        required=False
    )

    otp = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'OTP', 'class': 'form-control'}),
        required=False,
        max_length=6,
        min_length=6
    )

    redirect_url = forms.CharField(
        widget=forms.HiddenInput, required=False)

    def __init__(self, host, *args, **kwargs):
        self.host = host
        super().__init__(host, *args, **kwargs)

    def clean_redirect_url(self):
        url = self.cleaned_data['redirect_url'].strip()
        if url and is_safe_url(url, self.host):
            return url

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        otp = self.cleaned_data.get('otp')

        if not self.cleaned_data.get('password') and not self.cleaned_data.get('otp'):
            raise forms.ValidationError({
                "password": VALIDATION_ERROR_MESSAGES['PASSWORD_OR_OTP_REQUIRED'],
                "otp": VALIDATION_ERROR_MESSAGES['PASSWORD_OR_OTP_REQUIRED']
            })
        if password:
            self.user_cache = authenticate(self.request, mobile_number=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        else:
            self.user_cache = authenticate(self.request, mobile_number=username, otp=otp, strict_login_with_otp = True,)
            if self.user_cache is None:
                raise forms.ValidationError(
                    {
                        'otp': VALIDATION_ERROR_MESSAGES['INVALID_OTP'],
                    }
                )
            else:
                self.confirm_login_allowed(self.user_cache)


        return self.cleaned_data


class UserForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        kwargs['instance'] = user
        super().__init__(*args, **kwargs)
        if 'email' in self.fields:
            self.fields['email'].required = True
            self.fields['profile_picture'].widget = BootstrapClearableFileInput()

    def clean_email(self):
        """
        Make sure that the email address is always unique as it is
        used instead of the username. This is necessary because the
        uniqueness of email addresses is *not* enforced on the model
        level in ``django.contrib.auth.models.User``.
        """
        email = normalise_email(self.cleaned_data['email'])
        if User._default_manager.filter(
                email__iexact=email).exclude(id=self.user.id).exists():
            raise ValidationError(
                _("A user with this email address already exists"))
        # Save the email unaltered
        return email

    class Meta:
        model = User
        fields = existing_user_fields(['first_name', 'last_name', 'mobile_number', 'email', 'gender', 'dob', 'profile_picture'])


Profile = get_profile_class()
if Profile:  # noqa (too complex (12))

    class UserAndProfileForm(forms.ModelForm):

        def __init__(self, user, *args, **kwargs):
            try:
                instance = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                # User has no profile, try a blank one
                instance = Profile(user=user)
            kwargs['instance'] = instance

            super().__init__(*args, **kwargs)

            # Get profile field names to help with ordering later
            profile_field_names = list(self.fields.keys())

            # Get user field names (we look for core user fields first)
            core_field_names = set([f.name for f in User._meta.fields])
            user_field_names = ['email']
            for field_name in ('first_name', 'last_name'):
                if field_name in core_field_names:
                    user_field_names.append(field_name)
            user_field_names.extend(User._meta.additional_fields)

            # Store user fields so we know what to save later
            self.user_field_names = user_field_names

            # Add additional user form fields
            additional_fields = forms.fields_for_model(
                User, fields=user_field_names)
            self.fields.update(additional_fields)

            # Ensure email is required and initialised correctly
            self.fields['email'].required = True

            # Set initial values
            for field_name in user_field_names:
                self.fields[field_name].initial = getattr(user, field_name)

            # Ensure order of fields is email, user fields then profile fields
            self.fields.keyOrder = user_field_names + profile_field_names

        class Meta:
            model = Profile
            exclude = ('user',)

        def clean_email(self):
            email = normalise_email(self.cleaned_data['email'])

            users_with_email = User._default_manager.filter(
                email__iexact=email).exclude(id=self.instance.user.id)
            if users_with_email.exists():
                raise ValidationError(
                    _("A user with this email address already exists"))
            return email

        def save(self, *args, **kwargs):
            user = self.instance.user

            # Save user also
            for field_name in self.user_field_names:
                setattr(user, field_name, self.cleaned_data[field_name])
            user.save()

            return super().save(*args, **kwargs)

    ProfileForm = UserAndProfileForm
else:
    ProfileForm = UserForm