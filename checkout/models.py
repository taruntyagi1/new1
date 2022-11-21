from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import JSONField
from oscar.core.loading import get_class, get_model
from django.contrib.auth import get_user_model

Order = get_model("order", "Order")
User = get_user_model()

class UserTransaction(models.Model):
    """
    Transaction Model for store user payment information
    """

    PAYMENT_STATUS = (
        ('P', 'Paid'),
        ('F', 'Fail'),
        ('C', 'Created'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_transaction',
    )

    order_number = models.CharField(
        _("Order number"),
        max_length=128,
        unique=True,
        null=True,
        blank=True,
    )

    amount = models.FloatField(
        _("Amount"),
        default=0,
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        related_name='order_transaction',
        null=True,
        blank=True,
    )

    rz_order_id = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    rz_payment_id = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    razorpay_signature = models.TextField(
        null=True,
    )

    rz_response = JSONField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
    )


from oscar.apps.checkout.models import *  # noqa isort:skip