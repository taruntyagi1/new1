# python imports
import requests
import json

# django imports
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

@receiver(post_save, sender=User)
def populate_user(sender, instance, created, **kwargs):
    if created:
        try:
            if not instance.is_superuser and not instance.is_staff:
                if settings.DEBUG:
                    request_url = "http://localhost:8000/accounts/api/v1/trainee"
                else:
                    request_url = "http://staging.instafitness.in/accounts/api/v1/trainee"
                data = {
                    "user": {
                        "name": instance.full_name,
                        "mobile_number": instance.mobile_number.raw_input,
                        "email": instance.email
                    },
                }
                # res = requests.post(request_url, json=data)
        except:
            pass

