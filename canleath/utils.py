"""
    Functions used as a utility
"""

# python imports
import requests
from urllib.parse import urlencode
import binascii
import os

# django imports
from django.conf import settings
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# inner app imports
from basket.models import Basket

# third party imports
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework import exceptions

def send_sms_api(mobile_number, otp):
    """
    Sends Given Sms To Given Mobile
    """

    request_url = "https://2factor.in/API/V1/{}/SMS/{}/{}".format(settings.SMS_GATEWAY_API_KEY, mobile_number, otp)

    if not settings.DEBUG:
        resp = requests.get(request_url)
    else:
        print(request_url)


class BootstrapClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove File')
    template_name = 'customer/profile/bootstrap_clearable_file_input.html'


def generete_auth_token_key():
    """
    generate token for users
    """
    return binascii.hexlify(os.urandom(20)).decode()


def parse_basket_from_hyperlink(DATA, format):  # pylint: disable=redefined-builtin
    "Parse basket from relation hyperlink"
    basket_parser = HyperlinkedRelatedField(
        view_name="catalogue:basket-detail", queryset=Basket.objects, format=format
    )
    try:
        basket_uri = DATA.get("basket")
        data_basket = basket_parser.to_internal_value(basket_uri)
    except ValidationError as e:
        raise exceptions.NotAcceptable(e.messages)
    else:
        return data_basket


def get_first_and_last_name(name):
    """
    Returns first and last name from a given name
    """
    name = name.strip()
    name_parts = name.split()
    if len(name_parts) > 1:
        first_name = name_parts[0]
        last_name = ' '.join(name_parts[1:])
        return first_name, last_name
    return name, ''