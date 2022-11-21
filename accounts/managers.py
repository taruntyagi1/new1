# django imports
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    """
    custom manager for user
    """
    use_in_migrations = True

    def create_user(self, email, mobile_number, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and
        password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        if not mobile_number:
            raise ValueError('The given mobile number must be set')
        email = UserManager.normalize_email(email)
        user = self.model(
            email=email, mobile_number=mobile_number, is_staff=False, is_active=True,
            is_superuser=False,
            last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile_number, password, **extra_fields):
        u = self.create_user(email, mobile_number, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u