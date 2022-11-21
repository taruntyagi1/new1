# django imports
from django import forms
from django.contrib.auth import get_user_model

# oscar imports
from oscar.apps.dashboard.catalogue import forms as base_forms
from oscar.core.loading import get_model
from oscar.apps.catalogue.models import ProductClass

# third party imports
from treebeard.forms import movenodeform_factory

# inner app imports
from catalogue.models import (
    FAQSproduct,
    Who_we_are,
    Category,
    BannerImages,
    DietitionsAndNutritionists,
    Product,
    ProductReview,
    Micronutrientdeficiency,
    How_it_work,
    Our_products,
    Consult,
    Client_logo,
    Blog,
    Question,
    Frame1,
    Frame2,
    Frame3,
    Frame4,
    FaqIcon,
    Frame5,
    Header,
    Footer

   
    
)


User = get_user_model()

CategoryForm = movenodeform_factory(
    Category,
    fields=['name', 'description', 'image', 'icon', 'is_active', 'is_featured',],
)

class ProductForm(base_forms.ProductForm):
    """
    Customized Product Form
    """

    product_rating = forms.IntegerField(label='Rating', widget=forms.NumberInput, min_value=1, max_value=5)

    class Meta(base_forms.ProductForm.Meta):
        fields = (
            'title',
            'slug',
            'upc',
            'product_rating',
            'product_rating_count',
            'tagline',
            'product_title',
            'product_tagline',
            'product_benefit_image',
            'product_description',
            'program_detail',
            'product_banner_image',
            'description',
            'additional_information',
            'ingredients',
            'benefits',
            'product_benefit_1',
            'product_benefit_2',
            'unboxing_video_url',
            'meta_title',
            'meta_description',
            'meta_keywords',
            'is_discountable',
            'is_featured',
            'is_popular',
            'is_add_to_insta_eats',
            'is_add_to_gallery',
            'is_active',
            'is_latest_product',
            'structure',
            'diet_modification_dos',
            'diet_modification_donts',
            'lifestyle_modification_dos',
            'lifestyle_modification_donts',
            'nutritional_recommendation',
            'subscription_ordering',
            'show_in_subscription_plan'
        )

    def clean_slug(self):
        slug = self.cleaned_data.get('slug', None)
        if (slug and self.instance.pk and Product.objects.filter(slug=slug).exclude(id=self.instance.id).exists()) or not self.instance.id and Product.objects.filter(slug=slug).exists():
            raise forms.ValidationError('A Product with this slug is already exists')
        return slug
        


class CustomStockRecordForm(base_forms.StockRecordForm):
    """
    Customized Stock Record Form
    """

    class Meta(base_forms.StockRecordForm):
        fields = (
            'partner',
            'partner_sku',
            'price_currency',
            'price_excl_tax',
            'price_retail',
            'num_in_stock',
            'low_stock_threshold',
        )

    def __init__(self, *args, **kwargs):
        super(CustomStockRecordForm, self).__init__(*args, **kwargs)
        self.fields['partner'].required = True


class BannerImageForm(forms.ModelForm):
    """
    Banner Image Form
    """

    class Meta:
        model = BannerImages
        fields = (
            'image',
            'title',
            'subtitle',
            'hyperlink',
            'is_active',
        )


class ProductClassForm(forms.ModelForm):

    class Meta:
        model = ProductClass
        fields = ['name',]


class DietitionsAndNutritionistsForm(forms.ModelForm):
    """
    DietitionsAndNutritionists Form
    """
    product = forms.ModelChoiceField(required=False, queryset=Product.objects.filter(structure='parent'))

    class Meta:
        model = DietitionsAndNutritionists
        fields = (
            'product',
            'title',
            'description',
            'image',
            'url',
            'dietitions_and_nutritionists',
        )


class Who_we_areForm(forms.ModelForm):
    """
    Who_we_are Form
    """

    class Meta:
        model = Who_we_are
        fields = (
            'title',
            'description',
            'image',
            'image1',
            'image2',
            'image3',
            'image4',
            'hyperlink'
        )


class ProductReviewForm(forms.ModelForm):
    """
   ProductReview Form
    """
    
    product = forms.ModelChoiceField(required=False, queryset=Product.objects.filter(structure='parent'))


    class Meta:
        model = ProductReview
        fields = (
            'review',
            'product',
            'rating',
            'user',
            'user_name',
            'user_email',
            'thumbnail_image',
            'video_url',
            'is_approved',
            'is_featured',     
        )

    def clean(self):
        cleaned_data = super().clean()
        if not (cleaned_data.get('user') or (cleaned_data.get('user_name') and cleaned_data.get('user_email'))):
            raise forms.ValidationError({
                'user': "Either user should select or user name and email should be add if user is annonymous"
            })
        return cleaned_data    

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request') if 'request' in kwargs else None
        super(self.__class__, self).__init__(*args, **kwargs)   
        if request and request.method == 'GET':
            self.fields['user'].queryset = User.objects.none()
        if self.instance and self.instance.pk and self.instance.user:
            self.fields['user'].queryset = User.objects.filter(id=self.instance.user.id)  


class FAQSproductForm(forms.ModelForm):
    """
   FAQSproduct Form
    """
    product = forms.ModelChoiceField(required=False, queryset=Product.objects.filter(structure='parent'))


    class Meta:
        model = FAQSproduct
        fields = (
            'product',
            'question',
            'answer',
            'is_active',
        )


class FooterForm(forms.ModelForm):

    product = forms.ModelChoiceField(required = False, queryset = Product.objects.filter(structure = 'parent'))

    class Meta:
        model = Footer
        fields = (
            'image',
            'footer',
            'title',
            'links',
            'icon',
            'hyperlink',
            'is_active',
        )


class Client_logoForm(forms.ModelForm):
    """
     client_logo Form
    """
    product = forms.ModelChoiceField(required=False, queryset=Product.objects.filter(structure='parent'))


    class Meta:
        model = Client_logo
        fields = (
            'image',
            'is_active',
        )

class ConsultForm(forms.ModelForm):
    """
   CONSULT Form
    """
    product = forms.ModelChoiceField(required=False, queryset=Product.objects.filter(structure='parent'))


    class Meta:
        model = Consult
        fields = (
            'image',
            'title',
            'button',
            'is_active',
        )




class BlogForm(forms.ModelForm):

    product = forms.ModelChoiceField(required=False, queryset=Product.objects.filter(structure='parent'))
   

    class Meta:
        model = Blog
        fields =(
            'main_heading',
            'title',
            'description',
            'image',
            'is_active'
        )


class HeaderForm(forms.ModelForm):

    prodcut = forms.ModelChoiceField(required = False, queryset = Product.objects.filter(structure = "parent"))


    class Meta:

        model = Header
        fields =(

            'image',
            'title',
            'hyperlink',
            'icon',
            'is_active'
        )


class  MicronutrientdeficiencyForm(forms.ModelForm):

    product = forms.ModelChoiceField(required=False, queryset=Product.objects.filter(structure='parent'))
   

    class Meta:
        model = Micronutrientdeficiency
        fields =(
            
            'heading',
            'description',
            'is_active'
        )

class How_it_workForm(forms.ModelForm):

    product = forms.ModelChoiceField(required=False, queryset = Product.objects.filter(structure = 'parent'))

    class Meta:
        model = How_it_work
        fields = (

            
            'main_title',
            'title',
            'description',
            'title2',
            'description2',
            'title3',
            'description3',
            'is_active'
        )

class Our_productsForm(forms.ModelForm):

    product = forms.ModelChoiceField(required=False, queryset = Product.objects.filter(structure = 'parent'))

    class Meta:
        model = Our_products
        fields = (

            
            'image',
            'title',
            'is_active'
        )

class QuestionForm(forms.ModelForm):

    product = forms.ModelChoiceField(required=False, queryset = Product.objects.filter(structure = 'parent'))

    class Meta:
        model = Question
        fields = (

            
            'question',
            'answer',
            'is_active'
        )


class Frame1Form(forms.ModelForm):

    prodcut = forms.ModelChoiceField(required = False, queryset = Product.objects.filter(structure = "parent"))


    class Meta:

        model = Frame1
        fields =(

            'frames',
            'image',
            'title',
            'description',
            'is_active'
        )

class Frame2Form(forms.ModelForm):

    prodcut = forms.ModelChoiceField(required = False, queryset = Product.objects.filter(structure = "parent"))


    class Meta:

        model = Frame2
        fields =(

            'image',
            'title',
            'description',
            'is_active'
        )



class Frame3Form(forms.ModelForm):

    prodcut = forms.ModelChoiceField(required = False, queryset = Product.objects.filter(structure = "parent"))


    class Meta:

        model = Frame3
        fields =(

            'image',
            'title',
            'description',
            'is_active'
        )


class Frame4Form(forms.ModelForm):

    prodcut = forms.ModelChoiceField(required = False, queryset = Product.objects.filter(structure = "parent"))


    class Meta:

        model = Frame4
        fields =(

            'image',
            'title',
            'description1',
            'description2',
            'description3',
            'description4',
            'is_active'
        )



class FaqIconForm(forms.ModelForm):

    prodcut = forms.ModelChoiceField(required = False, queryset = Product.objects.filter(structure = "parent"))


    class Meta:

        model = FaqIcon
        fields =(

            'image',
            'step',
            'title',
            'description',
            'is_active'
        )



class Frame5Form(forms.ModelForm):

    prodcut = forms.ModelChoiceField(required = False, queryset = Product.objects.filter(structure = "parent"))


    class Meta:

        model = Frame5
        fields =(

            
            'title',
            'description',
            'choice',
            'is_active'
        )
