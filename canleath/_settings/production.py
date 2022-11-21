# staging settings

import os

SECRET_KEY = '-ojpfjqatdgbe-u+8i-2lavx&j&@4w=(%4b^h*-+c@jgaaqk!&'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'if_ecom',
        'USER': 'if_ecom',
        'PASSWORD': 'if_ecom',
        'HOST': 'localhost',
        'PORT': ''
    }
}

# DEFAULT_DOMAIN_NAME = 'canleath.staging.sudofire.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

# GOOGLE_MAPS_API_KEY = ''

# Email settings
EMAIL_HOST = 'email-smtp.ap-south-1.amazonaws.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'AKIAQ7UVLISMQON5EHCL'
EMAIL_HOST_PASSWORD = 'BJnO6dirtAKMhVzpsPxjhcXFyD4Ii5ZX24IcVavNF3mt'
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = 'if-ecom@sudofire.com'
SERVER_EMAIL = 'root.if-ecom-staging@sudofire.com'
EMAIL_SUBJECT_PREFIX = '[If Ecom Staging ]'

APPLICATION_HOST = ''
SERVER_HOST = ''
APPLICATION_PAYMENT_SUCCESS = "{host}/account/my-order".format(host=APPLICATION_HOST)
APPLICATION_PAYMENT_FAILURE = "{host}/payment-failure".format(host=APPLICATION_HOST)

# RAZORPAY_KEY = 'rzp_live_oIZKCQEB6221bL'
# RAZORPAY_SECRET = 'U73Pb3QH8h9WsrUiWpSgVnn3'

RAZORPAY_KEY = 'rzp_live_xj40QRdTTJGuS1'
RAZORPAY_SECRET = 'a5DtqmBBhFETMj6KcEH4TqFp'

INSTAEATS_URL = 'https://instaeats.in'

HOST_URL = 'https://instaeats.in'