# python imports
import requests
import json

# django imports
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.models import Q
from accounts.models import UserOTP
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    help = 'Set Permission'
    requires_migrations_checks = True

    is_next = False
    next_url = None
    def handle(self, *args, **options):
        if settings.DEBUG:
            request_url = "http://localhost:8000/accounts/api/v1/trainee"
        else:
            request_url = "http://staging.instafitness.in/accounts/api/v1/trainee"

        def populate_user(request_url=request_url):
            response = requests.get(request_url)
            data = response.json()
            trainee_list = data.get('results', None)
            if response.status_code == 200 and trainee_list:
                if data.get('next', None):
                    self.is_next=True
                    self.next_url=data.get('next')
                else:
                    self.is_next=False
                for obj in trainee_list:
                    user_object = obj.get("user")
                    first_name = user_object.get("first_name")
                    last_name = user_object.get("last_name") if user_object.get("last_name") else " "
                    mobile_number = user_object.get("mobile_number")
                    email = user_object.get("email")
                    gender = user_object.get("gender", None)
                    dob = user_object.get("dob", None)

                    exist_user = User.objects.filter(
                        Q(mobile_number=mobile_number)
                        |Q(email=email)
                    )

                    if not exist_user.exists():
                        user_obj = User.objects.create(
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            mobile_number=mobile_number,
                            gender=gender,
                            dob=dob,
                        )

                        otp = UserOTP.objects.get_or_create(
                            user=user_obj,
                            mobile_number=mobile_number,
                        )
                        self.stdout.write(self.style.SUCCESS("User with mobile number: {} and email: {} Added Successfully".format(user_obj.mobile_number, user_obj.email)))

                    else:
                        self.stdout.write(self.style.SUCCESS(
                            "User with mobile number: {} and email: {} are already exists".format(mobile_number, email)))

        populate_user(request_url=request_url)

        while self.is_next:
            request_url = self.next_url
            populate_user(request_url=request_url)
