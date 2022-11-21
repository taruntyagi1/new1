# python imports
import uuid
import os
import urllib.parse as urlparse

# django imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

from django.contrib.postgres.fields import ArrayField
from phonenumber_field.modelfields import PhoneNumberField

# oscar imports
from oscar.apps.catalogue.abstract_models import *
from accounts.models import User

# inner app imports
from canleath.messages import HELP_TEXTS

# local imports
from .choices import (
    MEDICAL_CONDITION, 
    SYMPTOMS_CHOICES,
)
from .utils import (
    convert_choice_to_dict,
)

def get_banner_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('banner_images/', filename)

def get_category_icon_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('category_icon/', filename)

def get_customer_testimonial_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('customer_testimonial/', filename)

def get_dietitians_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('dietitians and nutritionists/', filename)

# def get_blog_image_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = '{}.{}'.format(uuid.uuid4(), ext)
#     return os.path.join('blog_images/', filename)

def get_who_we_are_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('who_we_are_images/', filename)


def get_blog_image_path(instance, filename):
    ext  = filename.split(',')[-1]
    filename = '{},{}'.format(uuid.uuid4(),ext)
    return os.path.join('blog_images/', filename)

def get_product_benefit_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('product_benefit_images/', filename)

def get_review_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('review_images/', filename)



def get_our_products_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('our_products_images/', filename)

def get_client_logo_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('client_logo_images/', filename)

def get_about_us_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('about_us_images/', filename)

def get_faqicon_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('faqicon_images/', filename)

def get_header_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('header_images/', filename)


def get_footer_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('footer_images/', filename)









CUSTOMER_CHOICES = (
    ('Testimonial', ' Testimonial'),
    ('Follower', 'Follower'),
)

ABOUTUS_CHOICES = (
    ("our_mission", "our_mission"),
    ("our_vision", "our_vision")
)

FRAME_CHOICES = (
    ('Frame 1' , 'Frame 1'),
    ('Frame 2' , 'Frame 2'),
    ('Frame 3' , 'Frame 3'),
    ('Frame 4' , 'Frame 4'),
    ('Frame 5' , 'Frame 5'),

)

FOOTER_CHOICES = (
    ('Left_section', 'Left_section'),
    ('Quick_links', 'Quick_links'),
    ('More_links' , 'More_links'),
    ('Contact_us', 'Contact_us'),
)

DIETITIONS_CHOICES = (
    ('Dietitions', 'Dietitions'),
    ('Follower', 'Follower'),
)

class Category(AbstractCategory):
    """
    extended category model
    """

    image = models.ImageField(
        _('Image'),
        upload_to='categories',
        help_text=HELP_TEXTS['CATEGORY_IMAGE'],
        blank=True,
        null=True,
        max_length=255
    )

    icon = models.ImageField(
        _('Icon'),
        upload_to=get_category_icon_path,
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=False,
    )

    is_featured = models.BooleanField(
        _('Featured'),
        default=False
    )


class Product(AbstractProduct):
    """
    extended product model
    """

    product_rating = models.FloatField(
        _('Rating'),
        validators=[
            MinValueValidator(1,),
            MaxValueValidator(5,),
        ],
        null=True,
        blank=True
    )

    product_rating_count = models.PositiveIntegerField(
        _('Rating Count'),
        null=True,
        blank=True
    )

    tagline = models.CharField(
        _('Tagline'),
        max_length=40,
        null=True,
        blank=True,
    )

    product_tagline = models.CharField(
        _('Product Tagline'),
        max_length=100,
        null=True,
        blank=True,
    )

    product_benefit_image = models.ImageField(
        _('Product Benefit Image'),
        upload_to=get_product_benefit_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
    )

    product_description = models.TextField(
        _('Product Description'),
        null=True,
        blank=True,
    )

    program_detail = models.TextField(
        _('Program Detail'),
        null=True,
        blank=True,
    )

    product_banner_image = models.ImageField(
        _('Product Banner Image'),
        upload_to=get_banner_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
    )

    additional_information = models.TextField(
        _('Additional Information'),
        blank=True,
    )

    benefits = models.TextField(
        _('Benefits'),
        blank=True,
        null=True,
    )

    ingredients = models.TextField(
        _('Ingredients'),
        blank=True,
        null=True,
    )

    is_featured = models.BooleanField(
        _('Add to Featured Products'),
        default=False,
    )

    is_popular = models.BooleanField(
        _('Add to Popular Products'),
        default=False,
    )

    is_add_to_insta_eats = models.BooleanField(
        _('Add to InstaEats Section'),
        default=False,
    )

    is_add_to_gallery = models.BooleanField(
        _('Add to Gallery Section'),
        default=False,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    is_latest_product = models.BooleanField(
        _('Is Latest'),
        default=False,
    )

    product_title = models.CharField(
        _('Product Title'),
        max_length=100,
        null=True,
        blank=True,
    )

    product_benefit_1 = models.CharField(
        _('Product Benefit One'),
        max_length=100,
        null=True,
        blank=True,
    )

    product_benefit_2 = models.CharField(
        _('Product Benefit 2'),
        max_length=100,
        null=True,
        blank=True,
    )

    unboxing_video_url = models.URLField(
        _('Unboxing Video Url'),
        null=True,
        blank=True,
    )

    
    meta_title = models.CharField(
        _('Meta Title'),
        max_length=500,
        null=True,
        blank=True,
    )

    meta_description = models.TextField(
        _('Meta Description'),
        null=True,
        blank=True,
    )

    meta_keywords = ArrayField(
        models.CharField(
            _('Meta Keywords'),
            max_length=200,
            null=True,
            blank=True,
        ),
        null=True,
        blank=True,
    )

    diet_modification_dos = models.TextField(
        _("Diet Modification Do's"),
        null=True,
        blank=True,
    )

    diet_modification_donts = models.TextField(
        _("Diet Modification Dont's"),
        null=True,
        blank=True,
    )

    lifestyle_modification_dos = models.TextField(
        _("Lifestyle Modification Do's"),
        null=True,
        blank=True,
    )

    lifestyle_modification_donts = models.TextField(
        _("Lifestyle Modification Dont's"),
        null=True,
        blank=True,
    )
    
    nutritional_recommendation = models.TextField(
        _('Nutritional Recommendation'),
        null=True,
        blank=True,
    )

    subscription_ordering=models.IntegerField(
        default=0
    )

    show_in_subscription_plan=models.BooleanField(
        default=False
    )

    @property
    def round_rating(self):
        if self.product_rating:
            return round(self.product_rating)
        return 0

    @property
    def variants_list(self):
        product_list = []
        if self.is_parent:
            for prod in self.children.public().order_by('subscription_ordering'):
                if hasattr(prod, 'stockrecords') and prod.stockrecords.first() and prod.stockrecords.first().num_in_stock > 0:
                    product_list.append(prod)
        return product_list

    @property
    def percent_discount(self):
        discount = 0
        if hasattr(self, 'stockrecords') and self.stockrecords.first():
            discount = ((self.stockrecords.first().price_retail - self.stockrecords.first().price_excl_tax)*100)/self.stockrecords.first().price_retail
            discount = round(discount)
        return discount    

    @property
    def get_complete_title(self):
        if self.structure == "child":
            name = f"{self.parent.title} {self.title}"
        else:
            name = self.title
        return name      

    @property
    def get_tag_line(self):
        if self.structure == "child":
            name = self.parent.tagline
        else:
            name = self.tagline
        return name

    @property
    def video_id(self):
        parsed = urlparse.urlparse(self.unboxing_video_url)
        id_list = urlparse.parse_qs(parsed.query).get('v')
        return id_list[0] if id_list else None        


    def get_absolute_url(self):
        """
        Return a product's absolute URL
        """
        return reverse('website:product_detail',
                       kwargs={'slug': self.slug}) 

    def get_suggested_product(self):

        product_list = []
        if self.is_parent:
            for prod in self.children.public().filter(show_in_subscription_plan=True).order_by('subscription_ordering'):
                # if hasattr(prod, 'stockrecords') and prod.stockrecords.first() and prod.stockrecords.first().num_in_stock > 0:
                product_list.append(prod)
        return product_list                    



class BannerImages(models.Model):
    """
    model for banner images
    """

    image = models.ImageField(
        _('Banner Image'),
        upload_to=get_banner_image_path,
    )

    title = models.CharField(
        _('Title'),
        max_length=100,
        null=True,
        blank=True,
    )

    subtitle = models.CharField(
        _('Subtitle'),
        max_length=200,
        null=True,
        blank=True,
    )

    hyperlink = models.URLField(
        _('HyperLink'),
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    @property
    def sys_id(self):
        return 'BN{}'.format(str(self.id+1000).zfill(6))


class CustomerTestimonial(models.Model):
    """
    Customer Reviews
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        related_name="testimonial_product",
        null=True,
        blank=True
    )

    name = models.CharField(
        _('Name'),
        max_length=30,
    )

    customer_image = models.ImageField(
        _('Customer Image'),
        upload_to=get_customer_testimonial_path,
        null=True,
        blank=True,
    )

    review = models.TextField(
        _('Review')
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    timestamp = models.DateTimeField(
        _('Timestamp'),
        auto_now_add=True
    )

    city = models.CharField(
        _('City'),
        max_length=30,
        null=True,
        blank=True,
    )

    @property
    def sys_id(self):
        return 'CR{}'.format(str(self.id+1000).zfill(6))


class NewsLetter(models.Model):
    """
    model for news letter
    """

    email = models.EmailField(
        _('Email'),
    )

    @property
    def sys_id(self):
        return 'NL{}'.format(str(self.id+1000).zfill(6))


class DietitionsAndNutritionists(models.Model):
    """
    Customer Reviews
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        related_name="dietitions_product",
        null=True,
        blank=True
    )

    title = models.CharField(
        _('Title'),
        max_length=30,
        null=True,
        blank=True,
    )
    
    description = models.TextField(
        _('Description'),
        null=True,
        blank=True,
    )

    image = models.ImageField(
        _('Image'),
        upload_to=get_dietitians_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
    )

    url = models.URLField(
        _('HyperLink'),
        null=True,
        blank=True,
    )
    
    dietitions_and_nutritionists = models.CharField(
        _('Dietitions And Nutritionists'),
        max_length=30,
        choices=DIETITIONS_CHOICES
    )

    @property
    def sys_id(self):
        return 'DT{}'.format(str(self.id+1000).zfill(6))

    @property
    def video_id(self):
        parsed = urlparse.urlparse(self.url)
        id_list = urlparse.parse_qs(parsed.query).get('v')
        return id_list[0] if id_list else None    


class Who_we_are(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=2000,
        null=True,
        blank=True,
    )
    
    description = models.TextField(
        _('Description'),
        null=True,
        blank=True,
    )

    image = models.ImageField(
        _('Image'),
        upload_to=get_who_we_are_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
    )

    image1 = models.ImageField(
        _('Image1'),
        upload_to=get_who_we_are_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
    )

    image2 = models.ImageField(
        _('Image2'),
        upload_to=get_who_we_are_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
    )

    image3 = models.ImageField(
        _('Image3'),
        upload_to=get_who_we_are_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
    )

    image4 = models.ImageField(
        _('Image4'),
        upload_to=get_who_we_are_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
    )

    hyperlink = models.URLField(
        _('Hyperlink'),
        max_length=200,
        null=True,
        blank=True,

    )
    
    
    
    


class ProductReview(models.Model):
    """
    Product Customer Review Model
    """

    review = models.TextField(
        _("Review"),
        null=True,
        blank=True,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews_product"
    )

    rating = models.PositiveIntegerField(
        _("Rating"),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        blank=True,
        null=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='product_reviews',
        blank=True,
        null=True
    )

    user_name = models.CharField(
        _('Anonymous User Name (If user not selected)'),
        max_length=100,
        null=True,
        blank=True,
    )

    user_email = models.EmailField(
        _('Anonymous Email (If user not selected)'),
        null=True,
        blank=True,
    )

    thumbnail_image = models.ImageField(
        _(' Video Image'),
        upload_to=get_review_image_path,
        help_text=HELP_TEXTS['VIDEO_IMAGE'],
        null=True,
        blank=True,
    )
    
    video_url = models.URLField(
        _('HyperLink'),
        null=True,
        blank=True,
    )

    is_approved = models.BooleanField(
        _('Approved'),
        default=False,
    )

    is_featured = models.BooleanField(
        _('featured'),
        default=False,
    )

    created_on = models.DateTimeField(
        _('Created on'),
        auto_now_add=True,
    )

    edited_at = models.DateTimeField(
        _("Edited At"),
        auto_now=True
    )

    @property
    def sys_id(self):
        return "PR{}".format(str(self.pk + 1000).zfill(6))

    @property
    def video_id(self):
        parsed = urlparse.urlparse(self.video_url)
        id_list = urlparse.parse_qs(parsed.query).get('v')
        return id_list[0] if id_list else None        

    def __str__(self):
        return self.sys_id


class FAQSproduct(models.Model):
    """
    product faqsproduct
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        related_name="faqsproduct_product",
        null=True,
        blank=True
    )

    question = models.TextField(
        _('Question'),
        null=True,
        blank=True
    )

    answer = models.TextField(
        _('Answer'),
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    timestamp = models.DateTimeField(
        _('Timestamp'),
        auto_now_add=True
    )

    @property
    def sys_id(self):
        return 'FQ{}'.format(str(self.id+1000).zfill(6))


class Blog(models.Model):


    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="blog_product",
    null=True,
    blank=True
    )
    title = models.CharField(
        _('Title'),
        max_length=2000,
        null=True,
        blank=True,
    )
    
    description = models.CharField(
        _('Description'),
        max_length=2000,
        null=True,
        blank=True,
    )

    main_heading = models.CharField(
        _('Main_Heading'),
        max_length=10000,
        null=True,
        blank=True,
    )

    image = models.ImageField(
        _('Image'),
        upload_to=get_blog_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    
   
    @property
    def sys_id(self):
        return "Blog{}".format(str(self.pk + 1000).zfill(6))

class How_it_work(models.Model):
    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="how_it_work_product",
    null=True,
    blank=True
    )
    main_title = models.CharField(
        _('Main_Title'),
        max_length=10000,
        null=True,
        blank=True,
    )
    
   


    title = models.CharField(
        _('Title'),
        max_length=2000,
        null=True,
        blank=True,
    )
    
    description = models.TextField(
        _('Description'),
        null=True,
        blank=True,
    )

    title2 = models.CharField(
        _('Title2'),
        max_length=2000,
        null=True,
        blank=True,
    )
    
    description2 = models.TextField(
        _('Description2'),
        null=True,
        blank=True,
    )

    title3 = models.CharField(
        _('Title3'),
        max_length=2000,
        null=True,
        blank=True,
    )
    
    description3 = models.TextField(
        _('Description3'),
        null=True,
        blank=True,
    )

  
    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

     
    @property
    def sys_id(self):
        return "how_it_work{}".format(str(self.pk + 1000).zfill(6))




 
class Micronutrientdeficiency(models.Model):


    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="micronutrient_product",
    null=True,
    blank=True
    )
   
    heading = models.CharField(
        _('Heading'),
        max_length=2000,
        null=True,
        blank=True,
    )

 
    description = models.CharField(
        _('Description'),
        max_length=2000,
        null=True,
        blank=True,
    )
    

    
    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    
   
    @property
    def sys_id(self):
        return "Micronutrient{}".format(str(self.pk + 1000).zfill(6))
       
class Our_products(models.Model):


    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="our_products_product",
    null=True,
    blank=True
    )
    image = models.FileField(
        _('Image'),
        upload_to=get_our_products_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
        
    )

 
    title = models.CharField(
        _('Title'),
        max_length=2000,
        null=True,
        blank=True,
    )
    
   
    
    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    
   
    @property
    def sys_id(self):
        return "Client_logo{}".format(str(self.pk + 1000).zfill(6))

class Consult(models.Model):


    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="consult_product",
    null=True,
    blank=True
    )
    image = models.FileField(
        _('Image'),
        upload_to=get_blog_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
        
    )

 
    title = models.CharField(
        _('Title'),
        max_length=2000,
        null=True,
        blank=True,
    )
    button = models.CharField(
        _('Button'),
        max_length=2000,
        null=True,
        blank=True,
    )
    
   
    
    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    
   
    @property
    def sys_id(self):
        return "CONSULT{}".format(str(self.pk + 1000).zfill(6))


class FaqIcon(models.Model):


    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="faqicon_product",
    null=True,
    blank=True
    )
    image = models.ImageField(
        _('Image'),
        upload_to=get_faqicon_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
        
    )

    step = models.CharField(
        _('Step'),
        max_length=1000,
        null=True,
        blank=True,
        
    )

 
    title = models.CharField(
        _('Title'),
        max_length=20000,
        null=True,
        blank=True,
    )


    description = models.CharField(
        _('Description'),
        max_length=100000,
        null=True,
        blank=True,
    )
    
    
   
    
    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    
   
    @property
    def sys_id(self):
        return "FI{}".format(str(self.pk + 1000).zfill(6))


class Frame1(models.Model):
    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="frame1_product",
    null=True,
    blank=True
    )



    
    frames = models.CharField(
        _('Frames'),
        max_length=30,
        choices=FRAME_CHOICES,
        null = True,
        blank= True
    )

    image = models.ImageField(
       _("Image"),
        upload_to=get_about_us_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
        
    )

    title = models.CharField(
        _("Title"),
        max_length=1000,
        null = True,
        blank = True,
    )

    description = models.TextField(
        _("Description"),
      
        null = True,
        blank = True,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )


       
    @property
    def sys_id(self):
        return "F1{}".format(str(self.pk + 1000).zfill(6))

class Frame2(models.Model):
    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="frame2_product",
    null=True,
    blank=True
    )

    image = models.ImageField(
       _("Image"),
        upload_to=get_about_us_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
        
    )

    title = models.CharField(
        _("Title"),
        max_length=1000,
        null = True,
        blank = True,
    )

    description = models.TextField(
        _("Description"),
      
        null = True,
        blank = True,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )


       
    @property
    def sys_id(self):
        return "F2{}".format(str(self.pk + 1000).zfill(6))


class Frame3(models.Model):
    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="frame3_product",
    null=True,
    blank=True
    )

    image = models.ImageField(
       _("Image"),
        upload_to=get_about_us_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
        
    )

    title = models.CharField(
        _("Title"),
        max_length=1000,
        null = True,
        blank = True,
    )

    description = models.TextField(
        _("Description"),
      
        null = True,
        blank = True,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )


       
    @property
    def sys_id(self):
        return "F3{}".format(str(self.pk + 1000).zfill(6))


class Frame4(models.Model):
    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="frame4_product",
    null=True,
    blank=True
    )

    image = models.ImageField(
       _("Image"),
        upload_to=get_about_us_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
        
    )

    title = models.CharField(
        _("Title"),
        max_length=1000,
        null = True,
        blank = True,
    )

    description1 = models.TextField(
        _("Description1"),
      
        null = True,
        blank = True,
    )
    description2 = models.TextField(
        _("Description2"),
      
        null = True,
        blank = True,
    )
    description3 = models.TextField(
        _("Description3"),
      
        null = True,
        blank = True,
    )
    description4 = models.TextField(
        _("Description4"),
      
        null = True,
        blank = True,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )


       
    @property
    def sys_id(self):
        return "F4{}".format(str(self.pk + 1000).zfill(6))



class Frame5(models.Model):
    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="frame5_product",
    null=True,
    blank=True
    )

   
    title = models.CharField(
        _("Title"),
        max_length=1000,
        null = True,
        blank = True,
    )

    description = models.CharField(
        _("Description"),
        max_length=10000,
      
        null = True,
        blank = True,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    choice = models.CharField(
        _('Choice'),
        max_length=30,
        choices=ABOUTUS_CHOICES
    )


       
    @property
    def sys_id(self):
        return "F3{}".format(str(self.pk + 1000).zfill(6))




  




class Client_logo(models.Model):


    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="client_logo_product",
    null=True,
    blank=True
    )
    image = models.FileField(
        _('Image'),
        upload_to=get_client_logo_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
        
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    
    @property
    def sys_id(self):
        return "CL{}".format(str(self.pk + 1000).zfill(6))




class Header(models.Model):


    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="header_product",
    null=True,
    blank=True
    )
    image = models.FileField(
        _('Image'),
        upload_to=get_header_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
        
    )
    title  = models.CharField(
        _("Title"),
        max_length=100,
        null = True,
        blank = True
    )
    
    icon = models.CharField(
        _("Icon"),
        max_length=100,
        null = True,
        blank= True,
    )

    hyperlink = models.URLField(
        _('Hyperlink'),
        null = True,
        blank = True,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    
    @property
    def sys_id(self):
        return "HD{}".format(str(self.pk + 1000).zfill(6))


class Footer(models.Model):


    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="footer_product",
    null=True,
    blank=True
    )
    image = models.FileField(
        _('Image'),
        upload_to=get_header_image_path,
        help_text=HELP_TEXTS['IMAGE'],
        null=True,
        blank=True,
        
    )

    footer = models.CharField(
        _("Footer"),
        choices= FOOTER_CHOICES,
        max_length=1000,
        null = True,
        blank = True
    )
    title  = models.CharField(
        _("Title"),
        max_length=100,
        null = True,
        blank = True
    )

    links = models.CharField(
        _("Links"),
        max_length=1000,
        null = True,
        blank = True
    )
    
    icon = models.CharField(
        _("Icon"),
        max_length=100,
        null = True,
        blank= True,
    )

    hyperlink = models.URLField(
        _('Hyperlink'),
        null = True,
        blank = True,
    )

    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    
    @property
    def sys_id(self):
        return "HD{}".format(str(self.pk + 1000).zfill(6))


class Question(models.Model):


    product = models.ForeignKey(
    Product,
    on_delete=models.SET_NULL,
    related_name="question_product",
    null=True,
    blank=True
    )
   
    question = models.CharField(
        _('Question'),
        max_length=2000,
        null=True,
        blank=True,
    )

 
    answer = models.CharField(
        _('Answer'),
        max_length=10000,
        null=True,
        blank=True,
    )
    

    
    is_active = models.BooleanField(
        _('Active'),
        default=True,
    )

    
   
    @property
    def sys_id(self):
        return "FQ{}".format(str(self.pk + 1000).zfill(6))




class Questionaire(models.Model):
    
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    AGE = (
        ('0-16', '0-16'),
        ('17-40', '17-40'),
        ('41-70', '41-70'),
        ('71-100', '71-100')
    )

    name = models.CharField(
        _('Full Name'), 
        max_length=255, 
        blank=True,
        null=True
    )

    email = models.EmailField(
        _('Email Address'),
        blank=True,
        null=True
    )

    mobile_number = PhoneNumberField(
        _('Mobile Number'),
        null=True,
        blank=True
    )


    gender = models.CharField(
        _('Gender'),
        choices=GENDERS,
        max_length=10,
        null=True,
        blank=True,
    )

    age = models.CharField(
        _('Age'),
        choices=AGE,
        max_length=10,
        null=True,
        blank=True,
    )

    medical_condition = ArrayField(
        models.CharField(
            _('Medical Condition'),
            choices=MEDICAL_CONDITION,
            max_length=50,
            null=True,
            blank=True,
        ),
        blank=True,
        null=True,
    )
    
    symptoms = ArrayField(
        models.CharField(
            _('Symptoms'),
            choices=SYMPTOMS_CHOICES,
            max_length=50,
            null=True,
            blank=True,
        ),
        null=True,
        blank=True,
    )

    @property
    def sys_id(self):
        return 'DEFREP{}'.format(str(self.id+1000).zfill(6))

    @property
    def get_absolute_url(self):
        url = reverse('website:defficiency_report', kwargs={'pk': self.id})    
        return url

    def get_medical_condition(self):
        medical_condition_val_list = []
        if self.medical_condition:
            medical_condition_dict = convert_choice_to_dict(MEDICAL_CONDITION)
            for med in self.medical_condition:
                if med in medical_condition_dict:
                    medical_condition_val_list.append(medical_condition_dict[med])
        return medical_condition_val_list

    def get_symptoms_val(self):
        symptoms_val_list = []
        if self.symptoms:
            symptoms_dict = convert_choice_to_dict(SYMPTOMS_CHOICES)
            for sym in self.symptoms:
                if sym in symptoms_dict:
                    symptoms_val_list.append(symptoms_dict[sym])
        return symptoms_val_list                   

    def get_recommandation(self):
        
        problem = None
        recommendation = []
        dietry_suggesstion = None
        medical_con=['']
        if self.medical_condition:
            medical_con=self.medical_condition
        
        # if self.age == '17-40' and medical_con and len(medical_con) >= 2 and self.gender != 'Other':
        #     # case 12
        #     problem = 'Thyroid/ Diabetes/ Hypertension'
        #     recommendation = ['Thyro Health', 'Diabetes Health', 'Heart Health']
        if "PCOD" in medical_con and "Diabetes" in  medical_con and "Thyroid" not in medical_con and self.gender == 'Male':    
            # case 1
            problem = ''
            recommendation = ['Diabetes Health']   

        elif "PCOD" in medical_con and "Thyroid" not in medical_con and  self.gender == 'Female':    
            # case 2
            problem = ''
            recommendation = ['PCOS Health']     
        elif "PCOD" in medical_con and "Thyroid" not in medical_con and self.gender != 'Other':    
            
            problem = ''
            recommendation = ['PCOS Health']
        
        elif (self.age == '17-40' or  self.age == '41-70' or self.age == '71-100') and "Thyroid" in medical_con and self.gender != 'Other':    
            # case 6
            problem = ''
            recommendation = ['Thyro Health']  

        elif (self.age == '17-40' or  self.age == '41-70' or self.age == '71-100') and "Diabetes" in medical_con and "Thyroid"  not in medical_con and "PCOD" not in medical_con and self.gender != 'Other':    
            # case 7
            problem = ''
            recommendation = ['Diabetes Health']     

        elif (self.age == '17-40' or  self.age == '41-70' or self.age == '71-100') and "Skin Problems" in medical_con and self.gender != 'Other':
            # case 3
            problem = 'Acne/ Dullness/ Hairfall/ Pigmentation/ Dry Skin/ Dandruff/ Itchy Skin'
            recommendation = ['Skin Health']
        elif (self.age == '17-40' or  self.age == '41-70' or self.age == '71-100') and "Digestive Issues" in medical_con and self.gender != 'Other':
            # case 4
            problem = 'Constipation/ Acidity/ HeartBurn/ Gas formation'
            recommendation = ['Gut Health']   
        elif (self.age == '17-40' or  self.age == '41-70' or self.age == '71-100') and "Constipation" in medical_con and self.gender != 'Other':
            # case 5
            problem = 'Constipation/ Acidity/ HeartBurn/ Gas formation'
            recommendation = ['Gut Health'] 

        elif (self.age == '17-40' or  self.age == '41-70' or self.age == '71-100') and "Acidity" in medical_con and self.gender != 'Other':
            # case 6
            problem = 'Constipation/ Acidity/ HeartBurn/ Gas formation'
            recommendation = ['Gut Health']    
        
        elif (self.age == '17-40' or  self.age == '41-70' or self.age == '71-100') and "Hyperpigmenation" in medical_con and self.gender != 'Other':
            # case 7
            problem = 'Constipation/ Acidity/ HeartBurn/ Gas formation'
            recommendation = ['Skin Health']     

        elif (self.age == '17-40' or  self.age == '41-70' or self.age == '71-100') and "Heart diseases" in medical_con and self.gender != 'Other':
            # case 8
            problem = 'Hyperlipidmia/ Hypertension'    
            recommendation = ['Heart Health']
        
           
           
        elif self.age == '0-16' and self.gender != 'Other':    
            # case 9
            problem = ''
            recommendation = ['Kids Health']
        elif self.age == '41-70' or self.age == '71-100' and self.gender == 'Female':    
            # case 10
            problem = ''
            recommendation = ['Daily Health']
        elif self.age == '17-40' and self.gender == 'Female':    
            # case 11
            problem = ''
            recommendation = ["Women's Health"]
        elif self.age == '41-70' or self.age == '71-100' and self.gender == 'Male':    
            # case 12
            problem = ''
            recommendation = ['Daily Health'] 
        elif self.age == '17-40' and self.gender == 'Male':
            # case 13
            problem = ''
            recommendation = ["Men's Health"]
        recommendation = {
            'problem': problem,
            'recommendation': recommendation,
            'dietry_suggesstion': dietry_suggesstion,
        }       
        return recommendation
             

    def get_deficiency_report(self):
        deficiency_list = []
        deficiency_obj_list = []
        iron_symptoms = ["Fatigue", "Confusion", "Exhaustion", "Tiredness and Sleepiness", "Anemia", "coldness",
                         "Burning or sore tongue", "Cravings for non-nutritive substances", "Craving for Sugar", "Irregular hunger feeling"]
        magnesium_symptoms = ["Fatigue", "Exhaustion", "Tiredness and Sleepiness", "Muscle cramps", "Frequent Sweating", "Irregular Heartbeat", "Feeling Bloated"]      
        vitamin_b1_symptoms = ["Fatigue", "Confusion", "Exhaustion", "Tiredness and Sleepiness", "Nervousness", "Feeling Bloated",]
        vitamin_b2_symptoms = ["Fatigue", "Confusion", "Exhaustion", "Tiredness and Sleepiness", "Burning or sore tongue", "Cracked lips", "Dry skin", "Hair loss"]
        vitamin_c_symptoms = ["Fatigue", " Weakness", "Exhaustion","Tiredness and Sleepiness", "Slow wound Healing", "Nose bleeding"]
        folate_symptoms = ["Irritabilty",]
        vitamin_d_symptoms = ["Feeling of Depression, Anxiety, Stress", "Joint Pain", "Cramps in legs and muscles", "Pain and Weakness in Muscles", "Irregular hunger feeling"]
        vitamin_b6_symptoms = ["Feeling of Depression, Anxiety, Stress", "Hairfall", "Cracked lips", "Sensitive Skin and Acne"]
        zinc_symptoms = ["Slow wound Healing", "Loss of Appetite", "Loss of taste", "Craving for Sugar", "Hairfall", "Feeling Bloated"]
        vitamin_a_symptoms = ["Brittle Nails", "Dry & Damaged hair", "Sensitive Skin and Acne",]
        calcium_symptoms = ["Craving for Sugar", "Pain and Weakness in Muscles", "Craving for Snacks", "Irregular hunger feeling"]
        potassium_symptoms = ["Cramps in legs and muscles",]
        biotin_symptoms = ["Brittle Nails", "Dry skin", "Hairfall"]
        vitamin_b5_symptoms = ["Early graying of hair", "Slow wound Healing", "Sensitive Skin and Acne", "Hairfall"]
        vitamin_b12_symptoms = ["Burning or sore tongue", "Feeling of Depression, Anxiety, Stress", "Craving for Sugar", "Irregular hunger feeling"]
        vitamin_e_symptoms = ["Loss of Libido",]
        chromium_symptoms = ["Craving for Sugar",]
        sodium_symptoms = ["Craving for Snacks"]
        vitamin_k_symptoms = ["Nose bleeding"]
        selected_iron_symptoms = []
        selected_magnesium_symptoms = []
        selected_vitamin_b1_symptoms = []
        selected_vitamin_b2_symptoms = []
        selected_vitamin_c_symptoms = []
        selected_folate_symptoms = []
        selected_vitamin_d_symptoms = []
        selected_vitamin_b6_symptoms = []
        selected_zinc_symptoms = []
        selected_vitamin_a_symptoms = []
        selected_calcium_symptoms = []
        selected_potassium_symptoms = []
        selected_biotin_symptoms = []
        selected_vitamin_b5_symptoms = []
        selected_vitamin_b12_symptoms = []
        selected_vitamin_e_symptoms = []
        selected_chromium_symptoms = []
        selected_sodium_symptoms = []
        selected_vitamin_k_symptoms = []

        if self.symptoms:
            for sym in self.symptoms:
                if sym in iron_symptoms:
                    deficiency_list.append('Iron')
                    selected_iron_symptoms.append(sym)
                if sym in magnesium_symptoms:
                    deficiency_list.append('Magnesium')
                    selected_magnesium_symptoms.append(sym)
                if sym in vitamin_b1_symptoms:
                    deficiency_list.append('Vitamin B1')
                    selected_vitamin_b1_symptoms.append(sym)
                if sym in vitamin_b2_symptoms:
                    deficiency_list.append('Vitamin B2')
                    selected_vitamin_b2_symptoms.append(sym)
                if sym in vitamin_c_symptoms:
                    deficiency_list.append('Vitamin C')  
                    selected_vitamin_c_symptoms.append(sym)              
                if sym in folate_symptoms:
                    deficiency_list.append('Folate')    
                    selected_folate_symptoms.append(sym)
                if sym in vitamin_d_symptoms:
                    deficiency_list.append('Vitamin D') 
                    selected_vitamin_d_symptoms.append(sym)   
                if sym in vitamin_b6_symptoms:
                    deficiency_list.append('Vitamin B6')
                    selected_vitamin_b6_symptoms.append(sym)
                if sym in zinc_symptoms:
                    deficiency_list.append('Zinc')
                    selected_zinc_symptoms.append(sym)
                if sym in vitamin_a_symptoms:
                    deficiency_list.append('Vitamin A')  
                    selected_vitamin_a_symptoms.append(sym)          
                if sym in calcium_symptoms:
                    deficiency_list.append('Calcium')    
                    selected_calcium_symptoms.append(sym)
                if sym in potassium_symptoms:
                    deficiency_list.append('Potassium')    
                    selected_potassium_symptoms.append(sym)
                if sym in biotin_symptoms:
                    deficiency_list.append('Biotin')
                    selected_biotin_symptoms.append(sym)
                if sym in vitamin_b5_symptoms:
                    deficiency_list.append('Vitamin B5')    
                    selected_vitamin_b5_symptoms.append(sym)    
                if sym in vitamin_b12_symptoms:
                    deficiency_list.append('Vitamin B12')  
                    selected_vitamin_b12_symptoms.append(sym)  
                if sym in vitamin_e_symptoms:
                    deficiency_list.append('Vitamin E')  
                    selected_vitamin_e_symptoms.append(sym)  
                if sym in chromium_symptoms:
                    deficiency_list.append('Chromium')   
                    selected_chromium_symptoms.append(sym) 
                if sym in sodium_symptoms:
                    deficiency_list.append('Sodium')    
                    selected_sodium_symptoms.append(sym)
                if sym in vitamin_k_symptoms:
                    deficiency_list.append('Vitamin K')
                    selected_vitamin_k_symptoms.append(sym)
        deficiency_list = list(set(deficiency_list))    
   
        
        for deficiency in deficiency_list:
            if deficiency == "Iron":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_iron_symptoms,
                    # "consequences": "Iron deficiency can lead to many complications, including: \nStomach Ulcer, abnormally fast heartbeat (tachycardia) or heart failure, pregnancy complications, and developmental delays in children. ",
                    "consequences":"Iron deficiency can cause Stomach Ulcer, abnormally fast heartbeat (tachycardia) or heart failure."
                }
                deficiency_obj_list.append(deficiency_obj)
            elif deficiency == "Magnesium":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_magnesium_symptoms,
                    # "consequences": "Magnesium deficiency can lead to many complications, including: \nHigh blood pressure and heart disease, Diabetes, Osteoporosis, Pancreatitis & Migraine. ",
                    "consequences": "Magnesium deficiency can cause Hypertension,Diabetes & Osteoporosis. ",

                }
                deficiency_obj_list.append(deficiency_obj)   
            elif deficiency == "Vitamin B1":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_vitamin_b1_symptoms,
                    # "consequences": "Vitamin B1 deficiency can lead to many complications, including: \nHeart failure, Permanent nerve damage, Coma, Brain Diseases and Paralysis.",
                    "consequences":"Vitamin B1 deficiency can cause Heart failure, Permanent nerve damage, Coma. "
                }
                deficiency_obj_list.append(deficiency_obj)
            elif deficiency == "Vitamin B2":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_vitamin_b2_symptoms,
                    # "consequences": "Vitamin B2 deficiency can lead to many complications, including: \nDegeneration of the liver, Heart Diseases, Cancer, Nerve and muscle abnormalities and birth defects in infants.",
                    "consequences":"Vitamin B2 deficiency can cause  liver Degeneration, Heart Diseases, Cancer & birth defects in infants."
                }
                deficiency_obj_list.append(deficiency_obj)
            elif deficiency == "Vitamin C":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_vitamin_c_symptoms,
                    # "consequences": "Vitamin C deficiency can lead to many complications, including: \nLower extremity edema, and painful bleeding or effusions within joints, Irritability and Depression.",
                    "consequences":"Vitamin C deficiency can cause painful bleeding or effusions within joints, Irritability and Depression."
                }
                deficiency_obj_list.append(deficiency_obj)  
            elif deficiency == "Folate":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_folate_symptoms,
                    # "consequences": "Folate deficiency can lead to many complications, including: \nMegaloblastic anemia, Depression,  serious abnormalities in newborns, Insomnia and Angular Stomatitis (sores on corner of mouth).",
                     "consequences":"Folate deficiency can cause anemia, Depression,  serious abnormalities in newborns."
                }
                deficiency_obj_list.append(deficiency_obj)                    
            elif deficiency == "Vitamin D":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_vitamin_d_symptoms,
                    # "consequences": "Vitamin D deficiency can lead to many complications, including: \nDiabetes, High blood pressure, Cancer, Postural Deformities, Rickets in children, Weak Bones and Heart Failure",
                    "consequences":"Vitamin D deficiency can casue  Diabetes, High blood pressure, Cancer,  and Heart Failure"
                }
                deficiency_obj_list.append(deficiency_obj)                        
            elif deficiency == "Vitamin B6":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_vitamin_b6_symptoms,
                    # "consequences": "Vitamin B6 deficiency can lead to many complications, including: \nAnemia, Seizures, Heart stroke, Weakened immune system and anxiety.",
                    "consequences":"Vitamin B6 deficiency can cause Anemia, Seizures, Heart stroke, Weakened immune system."	
                }
                deficiency_obj_list.append(deficiency_obj)
            elif deficiency == "Zinc":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_zinc_symptoms,
                    # "consequences": "Zinc deficiency can lead to many complications, including: \nInfertility, Low Sperm Count, Weakened immune system, Prostate Cancer and Nervous Disorders.",
                    "consequences":"Zinc deficiency can casue Infertility, Low Sperm Count, and Prostate Cancer"
                }
                deficiency_obj_list.append(deficiency_obj)   
            elif deficiency == "Vitamin A":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_vitamin_a_symptoms,
                    # "consequences": "Vitamin A deficiency can lead to many complications, including: \nEye problems, Skin issues, Infertility, Growth issues in children & Respiratory tract infections",
                    "consequences":"Vitamin A deficiency can cause Infertility, Growth issues in children & Respiratory tract infections"
                }
                deficiency_obj_list.append(deficiency_obj)
            elif deficiency == "Calcium":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_calcium_symptoms,
                    # "consequences": "Calcium deficiency can lead to many complications, including: \nWeak Bones, Depression, Fractures, Heart Attack and High Blood Pressure.",
                    "consequences":"Calcium deficiency can cause Depression, Fractures, Heart Attack and High Blood Pressure."
                }
                deficiency_obj_list.append(deficiency_obj)               
            elif deficiency == "Potassium":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_potassium_symptoms,
                    # "consequences": "Potassium deficiency can lead to many complications, including: \nHigh Blood Pressure, Kidney Disease, Constipation, Heart Palpitations ,Muscle damage and Chronic Fatigue",
                    "consequences": "Potassium deficiency can cause High Blood Pressure, Kidney Disease & Heart Palpitations "
                }
                deficiency_obj_list.append(deficiency_obj)                                            
            elif deficiency == "Biotin":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_biotin_symptoms,
                    # "consequences": "Biotin deficiency can lead to many complications, including: \nChronic Fatigue, Hallucination, Hair loss (alopecia areata) and seizures.",
                    "consequences":"Biotin deficiency can cause Hallucination, Hair loss (alopecia areata) and seizures."
                }
                deficiency_obj_list.append(deficiency_obj)
            elif deficiency == "Vitamin B5":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_vitamin_b5_symptoms,
                    # "consequences": "Vitamin B5 deficiency can lead to many complications, including: \nBrain Fog, burning foot syndrome, Nerve degeneration, Depression and Digestive Issues.",
                    "consequences":"Vitamin B5 deficiency can cause Nerve degeneration, Depression and Digestive Issues."
                }
                deficiency_obj_list.append(deficiency_obj)                                               
            elif deficiency == "Vitamin B12":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_vitamin_b12_symptoms,
                    # "consequences": "Vitamin B12 deficiency can lead to many complications, including: \nMemory Loss, Anemia, Heart Palpitations, Depression and Digestive Issues and Paralysis.",
                    "consequences":"Vitamin B12 deficiency can casue  Anemia, Depression and Digestive Issues and Paralysis."
                }
                deficiency_obj_list.append(deficiency_obj)    
            elif deficiency == "Vitamin E":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_vitamin_e_symptoms,
                    # "consequences": "Vitamin E deficiency can lead to many complications, including: \nMuscle and Nerve Damage, Stroke, Loss of body movement control,  weakened immune system and Infertility",
                    "consequences":"Vitamin E deficiency can Cause Muscle and Nerve Damage, Stroke and Infertility"
                }
                deficiency_obj_list.append(deficiency_obj) 
            elif deficiency == "Chromium":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_chromium_symptoms,
                    # "consequences": "Chromium deficiency can lead to many complications, including: \nDiabetes, High Cholesterol levels, impaired coordination and Growth issues in children",
                    "consequences":"Chromium deficiency can cause Diabetes and Growth issues in children"
                }
                deficiency_obj_list.append(deficiency_obj)
            elif deficiency == "Sodium":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_sodium_symptoms,
                    # "consequences": "Sodium deficiency can lead to many complications, including: \nSeizures, Coma, Chronic Fatigue, Renal problems, Low Blood pressure and chronic Fatigue.",
                    "consequences":"Sodium deficiency can cause Seizures, Coma, Low Blood pressure and Renal problems."
                }
                deficiency_obj_list.append(deficiency_obj) 
            elif deficiency == "Vitamin K":
                deficiency_obj = {
                    "deficiency_name": deficiency,
                    "selected_symptoms": selected_vitamin_k_symptoms,
                    # "consequences": "Vitamin K deficiency can lead to many complications, including: \nExcessive Blood loss, Diabetes, Chronic Kidney Diseases and Heart Disease.",
                    "consequences":"Vitamin K deficiency can cause Excessive Blood loss, Chronic Kidney Diseases and Heart Disease."
                }
                deficiency_obj_list.append(deficiency_obj)   
        deficiency_report_data = {
            'deficiency_list': deficiency_list,
            'deficiency_obj_list': deficiency_obj_list
        }                                                                             
        return deficiency_report_data


from oscar.apps.catalogue.models import *  # noqa isort:skip


