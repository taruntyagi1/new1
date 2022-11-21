"""
Contains all the message sent from server side to the user
"""

ERROR_MESSAGES = {
    'DOCUMENT_EXIST': 'Document type already exist of this case.',
    'REQUIRED': 'Required',
    'PROTECTED_ERROR': 'Cannot delete "{0}: {1}" because it has object "{2}" linked to it.',
    'SELECT_MIN_ONE': 'Select minimum 1 item of {0}',
}

HELP_TEXTS = {
    "PROFILE PICTURE":"Please Upload a file in jpg, jpeg, png format only",
    "CATEGORY_IMAGE": 'Suggested Image Size is 1920x766',
    "IS_ACTIVE": 'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
    "PRODUCT_COLOR": 'If you are adding variants of this product. then you dont need to add color of this product',
    "IMAGE":'Suggested size 379x197px for dietitians and Suggested size 326x379 px for followers',
    "VIDEO_IMAGE":'Suggested Image Size is 1920x766'
}

EMAIL_MSG = {
    "CONTACT_EMAIL_SUBJECT": 'InstaEats Enquiry',
    "CONTACT_EMAIL_MESSAGE": 'Hi, You have received a query.\n Name : {} {} \n Email : {}\n Mobile Number : {} \n Query : {}',
}

SUCCESS_MESSAGES = {
    'NEWS_LETTER_SUBCRIPTION': 'You Have Subscribed Successfully',
    'CONTACT_US_SUCCESS_MESSAGE': 'Your query submitted successfully. We will contact you soon.',
    'OBJECTS_DELETED': '"{0}" item of {1} Deleted Successfully!!',
    'BANNER_IMAGE_ADDED' : 'Banner Images Added Created Successfully',
    'BANNER_IMAGE_UPDATE' : 'Banner Images Updated Successfully',
    'DIETITIANS_UPDATE' :'DietitionsAndNutritionists Updated Successfully',
    'PRODUCT_UPDATE' :'Product Updated Successfully',
    'CUSTOMER_TESTIMONIAL_ADDED' : 'Customer Testimonial Added Successfully',
    'CUSTOMER_TESTIMONIAL_UPDATE' : 'Customer Testimonial Updated Successfully',
    'COLOR_UPDATE' : 'Product Color Updated Successfully',
    'BLOG_UPDATE':'Blog updated Successfully',
    'ADDRESS_UPDATE':'Address Updated Successfully',
    'ADDRESS_CREATED':'Address Created Successfully',
    'ADDRESS_DELETE':'Address Deleted Successfully',
}

SMS_TEXTS = {
    'OTP': '{otp} is your OTP for {purpose} on Canleath. OTP is confidential never share with anyone.',
    'CUSTOMER_WELCOME_SMS': 'Hi {user}! Welcome to Canleath! This is the confirmation SMS regarding signup.'
}

VALIDATION_ERROR_MESSAGES = {
    'UNREGISTERED_MOBILE': 'A User With this number is not registered',
    'INVALID_MOBILE_NUMBER': 'Invalid Mobile Number or otp',
    'INVALID_NAME': 'Only alphabets are allowed',
    'PASSWORD_OR_OTP_REQUIRED': 'Password or OTP required',
    'INVALID_OTP': 'Please Enter Valid OTP',
    'MOBILE_NUMBER_REQUIRED': 'Mobile number is required for user',
    'FIRST_NAME_REQUIRED': 'First Name is required for user',
}

