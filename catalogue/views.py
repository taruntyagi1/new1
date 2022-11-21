# python imports
from itertools import zip_longest
from django.conf import settings
from django.db.models import Case, Value, When
from django.db import models
from urllib.parse import quote

# oscar imports
from oscar.apps.catalogue.views import (
    CatalogueView,
    ProductCategoryView,
    ProductDetailView,
)
from oscar.core.loading import (
    get_model,
    get_class,
)

# django imports
from django.views.generic import (
    ListView,
    TemplateView,
    FormView,
)
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, Http404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import (
    Q,
    Max,
)
from django.urls import reverse_lazy
from django.core.mail import send_mail
from basket.utils import lead_create

#inner imports
from canleath.messages import (
    SUCCESS_MESSAGES,
    VALIDATION_ERROR_MESSAGES,
    ERROR_MESSAGES,
    EMAIL_MSG,
)

# local imports
from .models import (

    Category,
    DietitionsAndNutritionists,
    Product,
    BannerImages,
    CustomerTestimonial,
    ProductReview,
    Micronutrientdeficiency,
    How_it_work,
    Who_we_are,
    Blog,
    Header
)
from .forms import (
    ContactUsForm,
    NewsLetterForm,
)

StockRecord = get_model('partner', 'StockRecord')

class ProductListView(ListView):
    """
    A view for display all the product in a website
    """
    model = Product
    template_name = 'catalogue/product_list.html'
    paginate_by = 20
    total_product = 0

    def get_queryset(self):
        queryset = self.model.objects.filter(is_active=True).exclude(structure='child')

        if self.request.GET.getlist('category'):
            get_category_list = self.request.GET.getlist('category')
            queryset = queryset.filter(categories__slug__in=get_category_list).distinct()
        
        if self.request.GET.getlist('cat'):
            get_category = self.request.GET.get('cat')
            queryset = queryset.filter(categories__name=get_category).distinct()

        if self.request.GET.get('is_latest_product', None) == '1':
            queryset = queryset.filter(is_latest_product=True)

        if self.request.GET.get('min_price') and self.request.GET.get('max_price'):
            min_price = int(self.request.GET.get('min_price'))
            max_price = int(self.request.GET.get('max_price'))
            queryset = queryset.filter(stockrecords__price_excl_tax__range=[min_price,max_price])
        
        if self.request.GET.get('price'):
            price_range = self.request.GET.get('price').split('-')
            if len(price_range) > 1:
                nemuric_price_range = [int(price) for price in price_range]
                queryset = queryset.filter(children__stockrecords__price_excl_tax__range=nemuric_price_range).distinct()
            else:
                queryset = queryset.filter(children__stockrecords__price_excl_tax__gte=price_range[0]).distinct()
        

        if self.request.GET.get('sort_by'):
            get_list = self.request.GET.get('sort_by')
            queryset = queryset.filter(children__title=get_list)


        if self.request.GET.get('q'):
            get_list = self.request.GET.get('q')
            queryset = queryset.filter(
                Q(title__icontains=get_list)
                |Q(description__icontains=get_list)
                |Q(children__title__icontains=get_list)
            ).distinct()
        
        
        
        if self.request.GET.get('order_by'):
            
            get_list = self.request.GET.get('order_by')
            if get_list == 'is_featured':
                queryset = queryset.filter(is_featured=True).distinct()
            
            if get_list == 'is_latest_product':
                queryset = queryset.filter(is_latest_product=True).distinct()

            if get_list == 'is_popular':
                queryset = queryset.filter(is_popular=True).distinct()


        if self.request.GET.get('sortby', None):
            sortby_str = self.request.GET.get('sortby')
            queryset = queryset.order_by(sortby_str)
        else:
            queryset = queryset.order_by('-date_created')

            self.total_product = queryset.count()

        return queryset.distinct()


    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        max_price = StockRecord.objects.aggregate(Max('price_retail')).get('price_retail__max')
        if max_price:
            context['max_price'] = int(max_price) + 500
        context['category_list'] = Category.objects.filter(depth=1, is_active=True)
        context['popular_product'] = Product.objects.filter(is_popular=True, is_active=True)
        context['total_product'] = self.total_product
        context['customer_testimonial_list'] = CustomerTestimonial.objects.filter(is_active=True)
        if self.request.GET.getlist('category'):
            get_category_list = self.request.GET.getlist('category')
            context['search_category'] = [i for i in get_category_list]
            if len(get_category_list) == 1:
                context['current_category'] = Category.objects.filter(slug=get_category_list[0]).first()
        return context


class HomepageView(CatalogueView):
    """
    A view for display all the product in a website
    """
    template_name = 'catalogue/homepage1.html'
    # template_name = 'website/new_templates/homepage.html'

    # def get_gallery_category_list(self):
    #     category_list = Category.objects.all()
    #     gallery_category = []
    #     for obj in category_list:
    #         if obj.product_set.filter(is_add_to_gallery=True).exists():
    #             gallery_category.append(obj)
    #     return gallery_category

    # def get_featured_product_with_category(self):
    #     featured_category = Category.objects.filter(is_featured=True)
    #     data_list = []
    #     for obj in featured_category:
    #         featured_product = obj.product_set.filter(is_featured=True)
    #         if featured_product.exists():
    #             data_dict = {
    #                 'category': obj,
    #                 'products': featured_product,
    #             }
    #             data_list.append(data_dict)
    #     return data_list        

    # def get_product_with_category(self):
    #     category = Category.objects.filter(product__isnull=False).distinct()
    #     data_list = []
    #     for obj in category:
    #         product = obj.product_set.filter(structure='parent')
    #         if product.exists():
    #             data_dict = {
    #                 'category': obj,
    #                 'products': product,
    #             }
    #             data_list.append(data_dict)
    #     return data_list        


    def get_context_data(self, *args, **kwargs):
        context = super(HomepageView, self).get_context_data(*args, **kwargs)
        context['featured_product'] = Product.objects.filter(is_featured=True).exclude(structure='child')
        # context['popular_product'] = Product.objects.filter(is_popular=True).exclude(structure='child')
        # context['insta_eats_product'] = Product.objects.filter(is_add_to_insta_eats=True).exclude(structure='child')
        # context['gallery_product'] = Product.objects.filter(is_active=True, is_add_to_gallery=True).exclude(structure='child')
        context['banner_images'] = BannerImages.objects.filter(is_active=True)
        # context['gallery_category_list'] = self.get_gallery_category_list()
        context['customer_testimonial_list'] = CustomerTestimonial.objects.filter(is_active=True)
        # context['category_with_product'] = self.get_product_with_category()
        context['dietitions_and_nutritionists'] = DietitionsAndNutritionists.objects.filter(dietitions_and_nutritionists='Dietitions')
        # context['followers'] = DietitionsAndNutritionists.objects.filter(dietitions_and_nutritionists='Follower')
        # context['featured_category_with_product'] = self.get_featured_product_with_category()
        # context['form'] = NewsLetterForm
        return context

    # def post(self, request, *args, **kwargs):
    #     news_letter_form = NewsLetterForm(request.POST, request.FILES)
    #     if news_letter_form.is_valid():
    #         news_letter_form.save()
    #         messages.add_message(request, messages.SUCCESS,
    #                              SUCCESS_MESSAGES['NEWS_LETTER_SUBCRIPTION'])
    #         return HttpResponseRedirect(reverse_lazy('catalogue:index'))
    #     context = {
    #         'form': news_letter_form
    #     }
    #     return self.render_to_response(context)


class ProductDetailsView(ProductDetailView):
    """
    A view for display all the product in a website
    """
    # template_name = 'catalogue/detail.html'
    template_name = 'website/new_templates/detail_page.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'


    # def redirect_if_necessary(self, current_path, product):
    #     if 'product-new' not in current_path:
    #         if self.enforce_parent and product.is_child:
    #             return HttpResponsePermanentRedirect(
    #                 product.parent.get_absolute_url())

    #         if self.enforce_paths:
    #             expected_path = product.get_absolute_url()
    #             if expected_path != quote(current_path):
    #                 return HttpResponsePermanentRedirect(expected_path)
    #     else:
    #         self.template_name = self.template_name_2            

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailsView, self).get_context_data(*args, **kwargs)
        
        context['dietitions_and_nutritionists'] = DietitionsAndNutritionists.objects.filter(dietitions_and_nutritionists='Dietitions', product=self.object)
        # video_products = ProductReview.objects.filter(Q(product=self.object))
        video_products = ProductReview.objects.all().annotate(custom_order=Case(
            When(product=self.object, then=Value(1)),
            default=Value(2),
            output_field=models.IntegerField(),
        )).order_by("custom_order")
        
        context['product_review'] = video_products.filter(Q(video_url=None)|Q(video_url=''))
        context['video_review'] = video_products.exclude(Q(video_url=None)|Q(video_url=''))
        context['customer_testimonial_list'] = CustomerTestimonial.objects.filter(is_active=True, product=self.object)

        return context        


class SiteLatestProductView(CatalogueView):
    """
    List View for Latest Product
    """

    template_name = 'catalogue/site_latest_product.html'


class AboutUsView(TemplateView):
    """
    AboutUs View
    """

    template_name = 'catalogue/about-us.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutUsView, self).get_context_data(*args, **kwargs)
        
  
        context['customer_testimonial_list'] = CustomerTestimonial.objects.filter(is_active=True)
      
        return context



class ContactUsView(SuccessMessageMixin, FormView):
    """
    ContactUs View
    """
    success_message = SUCCESS_MESSAGES['CONTACT_US_SUCCESS_MESSAGE']
    form_class = ContactUsForm
    template_name = 'catalogue/contact-us.html'
    success_url = reverse_lazy('website:contact_us')

    def form_valid(self, form):

        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        message = form.cleaned_data.get('message')
        recipient = ['info@instaeats.in',]
        subject = EMAIL_MSG['CONTACT_EMAIL_SUBJECT']
        message = EMAIL_MSG['CONTACT_EMAIL_MESSAGE'].format(first_name, last_name, email, phone, message)
        send_mail(subject, message , from_email=None,recipient_list=recipient)
        lead = {
            'first_name':first_name,
            'last_name':last_name,
            'mobile_number':phone,
        }
        lead_create(lead)
        return super(self.__class__, self).form_valid(form)


class PrivacyPolicyView(TemplateView):
    """
    PrivacyPolicy View
    """
    template_name = 'catalogue/privacy-policy.html'

class TermsOfUseView(TemplateView):
    """
    TermsOfUse View
    """
    template_name = 'catalogue/terms-of-use.html'


class ReturnPolicyView(TemplateView):
    """
    ReturnPolicy View
    """
    template_name = 'catalogue/return_policy.html'


class ShippingPolicyView(TemplateView):
    """
    ShippingPolicy View
    """
    template_name = 'catalogue/shipping_policy.html'


class FaqView(TemplateView):
    """
    Faq View
    """
    template_name = 'catalogue/faq.html'

class BlogView(TemplateView):

    tamplate_name = 'catalogue/blog.html'


class Who_we_areView(TemplateView):
    """
    Blog View
    """
    template_name = 'catalogue/blog.html'

class HeaderView(TemplateView):
    "Header view"
    template_name = 'catalogue/header.html'


class Who_we_areDetailView(TemplateView):
    """
    Blog DetailView
    """
    template_name = 'catalogue/blog_detail.html'
    

# class BlogView(ListView):
#     """
#     A view for display all the bog in a website
#     """
#     model = Product
#     template_name = 'catalogue/blog.html'
#     paginate_by = 10
#     total_product = 0

#     def get_queryset(self):
#         queryset = self.model.objects.all()
#         return queryset

class BasketItemDetailView(TemplateView):
    """
    basket item detail
    """    
    template_name = 'catalogue/partials/basket_item_detail.html'


def customer_review():
    product_reviews = ProductReview.objects.all()
    total_rating_5 = 0
    rating_count_5 = 0
    rating_count_4 = 0
    total_rating_4 = 0
    rating_count_3 = 0
    total_rating_3 = 0
    rating_count_2 = 0
    total_rating_2 = 0
    rating_count_1 = 0
    total_rating_1 = 0
    avg_rating = 0
    if product_reviews:
        for review in product_reviews:
            if review.rating == 5:
                rating_count_5 += review.rating
                total_rating_5 += 1
            if review.rating == 4:
                rating_count_4 += review.rating
                total_rating_4 += 1
            if review.rating == 3:
                rating_count_3 += review.rating
                total_rating_3 += 1
            if review.rating == 2:
                rating_count_2 += review.rating
                total_rating_2 += 1
            if review.rating == 1:
                rating_count_1 += review.rating
                total_rating_1 += 1

    total_rating_count = total_rating_5+total_rating_4+total_rating_3+total_rating_2+total_rating_1
    
    total_rating = rating_count_5+rating_count_4+rating_count_3+rating_count_2+rating_count_1
    if total_rating_count > 0:
        avg_rating = total_rating/total_rating_count
    percent_for_rating_5 = 0
    percent_for_rating_4 = 0
    percent_for_rating_3 = 0
    percent_for_rating_2 = 0
    percent_for_rating_1 = 0

    if total_rating_5 > 0:
        percent_for_rating_5 = (rating_count_5*100)/(total_rating_5*5)
    if total_rating_4 > 0:
        percent_for_rating_4 = (rating_count_4*100)/(total_rating_4*5)
    if total_rating_3 > 0:
        percent_for_rating_3 = (rating_count_3*100)/(total_rating_3*5)
    if total_rating_2 > 0:
        percent_for_rating_2 = (rating_count_2*100)/(total_rating_2*5)
    if total_rating_1 > 0:
        percent_for_rating_1 = (rating_count_1*100)/(total_rating_1*5)
    dic = {
        'avg_rating':avg_rating,
        'percent_for_rating_5':percent_for_rating_5,
        'percent_for_rating_4':percent_for_rating_4,
        'percent_for_rating_3':percent_for_rating_3,
        'percent_for_rating_2':percent_for_rating_2,
        'percent_for_rating_1':percent_for_rating_1,
        'total_rating':total_rating_count
    }

    return dic


class ReviewView(ListView):
    """
    Review View
    """
    
    model = ProductReview
    template_name = 'catalogue/review.html'

    def get_queryset(self):
        queryset = self.model.objects.all()

        if self.request.GET.get('product'):
            product = self.request.GET.get('product')
            queryset = queryset.filter(product__title=product).distinct()
        
        return queryset 

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['rating_data'] = customer_review()
        context['video_review'] = ProductReview.objects.exclude(Q(video_url=None)|Q(video_url='')).order_by('-created_on')
        context['text_review'] = ProductReview.objects.filter(Q(video_url=None)|Q(video_url='')).order_by('-created_on')
        return context


class CategoryProductListView(TemplateView):
    
    template_name = 'catalogue/partials/category_product_list.html'

    def get_product_with_category(self):
        category = Category.objects.filter(product__isnull=False).distinct()
        data_list = []
        for obj in category:
            product = obj.product_set.filter(structure='parent')
            if product.exists():
                data_dict = {
                    'category': obj,
                    'products': product,
                }
                data_list.append(data_dict)
        return data_list        


    def get_context_data(self, *args, **kwargs):
        context = super(CategoryProductListView, self).get_context_data(*args, **kwargs)
        context['category_with_product'] = self.get_product_with_category()
        context['instaeats_url'] = settings.INSTAEATS_URL
        return context

   

class DieticianDetailView(CatalogueView):
    """
    A view for display all the product in a website
    """
    template_name = 'catalogue/partials/dietician_detail.html'



class ProductListFilterView(ListView):
    """
    A view for display all the product in a website
    """
    model = Product
    template_name = 'catalogue/partials/product_list_filter.html'
    paginate_by = 20
    total_product = 0

    def get_queryset(self):
        queryset = self.model.objects.filter(is_active=True).exclude(structure='child')
        if self.request.GET.getlist('category'):
            get_category_list = self.request.GET.getlist('category')
            queryset = queryset.filter(categories__slug__in=get_category_list).distinct()
        
        if self.request.GET.getlist('cat'):
            get_category = self.request.GET.get('cat')
            queryset = queryset.filter(categories__name=get_category).distinct()

        if self.request.GET.get('is_latest_product', None) == '1':
            queryset = queryset.filter(is_latest_product=True)

        if self.request.GET.get('price'):
            price_range = self.request.GET.get('price').split('-')
            if len(price_range) > 1:
                nemuric_price_range = [int(price) for price in price_range]
                queryset = queryset.filter(children__stockrecords__price_excl_tax__range=nemuric_price_range).distinct()
            else:
                queryset = queryset.filter(children__stockrecords__price_excl_tax__gte=price_range[0]).distinct()

        if self.request.GET.get('sort_by'):
            get_list = self.request.GET.get('sort_by')
            queryset = queryset.filter(children__title=get_list)


        if self.request.GET.get('q'):
            get_list = self.request.GET.get('q')
            queryset = queryset.filter(
                Q(title__icontains=get_list)
                |Q(description__icontains=get_list)
                |Q(children__title__icontains=get_list)
            ).distinct()
        
        

        if self.request.GET.get('order_by'):
           
            get_list = self.request.GET.get('order_by')
            if get_list == 'is_featured':
                queryset = queryset.filter(is_featured=True).distinct()
            
            if get_list == 'is_latest_product':
                queryset = queryset.filter(is_latest_product=True).distinct()

            if get_list == 'is_popular':
                queryset = queryset.filter(is_popular=True).distinct()


        if self.request.GET.get('sortby', None):
            sortby_str = self.request.GET.get('sortby')
            queryset = queryset.order_by(sortby_str)
        else:
            queryset = queryset.order_by('-date_created')

            self.total_product = queryset.count()

        return queryset.distinct()


    def get_context_data(self, **kwargs):
        context = super(ProductListFilterView, self).get_context_data(**kwargs)
        max_price = StockRecord.objects.aggregate(Max('price_retail')).get('price_retail__max')
        if max_price:
            context['max_price'] = int(max_price) + 500
        context['category_list'] = Category.objects.filter(depth=1, is_active=True)
       
        if self.request.GET.getlist('category'):
            get_category_list = self.request.GET.getlist('category')
            context['search_category'] = [i for i in get_category_list]
            if len(get_category_list) == 1:
                context['current_category'] = Category.objects.filter(slug=get_category_list[0]).first()
        return context


class DietitianAdviceListView(TemplateView):
    """
    Dietitian List view
    """
    template_name = 'catalogue/dietitian_advice_list.html'

    def get_context_data(self, **kwargs):
        context = super(DietitianAdviceListView, self).get_context_data(**kwargs)
        context['dietitions_and_nutritionists'] = DietitionsAndNutritionists.objects.filter(dietitions_and_nutritionists='Dietitions')
        return context