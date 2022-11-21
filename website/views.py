from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    TemplateView,
    DetailView,
)
from oscar.apps.catalogue.views import ProductDetailView

from catalogue.models import (Questionaire, Product,CustomerTestimonial, DietitionsAndNutritionists,
   FAQSproduct,
    Category,
    DietitionsAndNutritionists,
    Product,
    BannerImages,
    Who_we_are,
    CustomerTestimonial,
    Blog,
    Micronutrientdeficiency,
    How_it_work,
    Our_products,
    Consult,
    Client_logo,
    Question,
    FaqIcon,
    Frame1,
    Frame2,
    Frame3,
    Frame4,
    Frame5,
    Header,

    ProductReview)
from django.db import models    
from django.db.models import Case, Value, When    
from django.contrib.messages.views import SuccessMessageMixin    
from oscar.core.loading import (
    get_model,
    get_class,
)    

from canleath.messages import (
    SUCCESS_MESSAGES,
    VALIDATION_ERROR_MESSAGES,
    ERROR_MESSAGES,
    EMAIL_MSG,
)

from django.urls import reverse_lazy
from django.core.mail import send_mail
from basket.utils import lead_create
from django.db.models import (
    Q,
    Max,
)    
from wkhtmltopdf.views import PDFTemplateView
from django.views.generic import (
    ListView,
    TemplateView,
    FormView,
)

from catalogue.forms import (
    ContactUsForm,
    NewsLetterForm,
)

StockRecord = get_model('partner', 'StockRecord')

# Create your views here.


class RobotsView(TemplateView):
    """
    Robots view
    """
    template_name = 'robots.txt'


class SitemapView(TemplateView):
    """
    Sitemap view
    """

    template_name = 'sitemap.xml'

class DefficiencyAssessmentView(TemplateView):
    """
    view for collect data of deffiency and prepare report accordingly
    """
    template_name = 'website/new_templates/defficiency_assessment.html'


class DeffieicencyReportView(DetailView):    
    """
    view for show deficiency report
    """
    model = Questionaire
    template_name = 'website/new_templates/assessment_report.html'

    def get_recommended_product(self):
        product_recommendation_list = []
        obj = self.get_object()
        recommendation_data = obj.get_recommandation()
        for rec_item in recommendation_data.get('recommendation'):
            prod_obj_list = Product.objects.browsable().filter(title__startswith=rec_item)
            product_recommendation_list = product_recommendation_list + list(prod_obj_list)
        if len(product_recommendation_list) > 0:
            return product_recommendation_list[0]    
        return None    


    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['recommended_product'] = self.get_recommended_product()
        return context


# class DeffieicencyReportPdfView(TemplateView):
class DeffieicencyReportPdfView(PDFTemplateView):
    """
    pdf view for deficiency report
    """
    template_name = 'website/new_templates/assessment_report_pdf.html'
    cmd_options={'margin-top': 5, 'enable_local_file_access': True}
    filename = 'deficiency-report.pdf'
    show_content_in_browser=True

    def get_object(self):
        report_obj = get_object_or_404(Questionaire, id=self.kwargs['pk'])
        return report_obj

    def get_recommended_product(self):
        product_recommendation_list = []
        obj = self.get_object()
        recommendation_data = obj.get_recommandation()
        for rec_item in recommendation_data.get('recommendation'):
            prod_obj_list = Product.objects.browsable().filter(title__startswith=rec_item)
            product_recommendation_list = product_recommendation_list + list(prod_obj_list)
        if len(product_recommendation_list) > 0:
            return product_recommendation_list[0]    
        return None      

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)    
        context['object'] = self.get_object()
        context['recommended_product'] = self.get_recommended_product()
        return context



class DeffieicencyPdfReportPdfView(TemplateView):
    """
    pdf view for deficiency report
    """
    template_name = 'website/new_templates/assessment_report_pdf.html'
    cmd_options={'margin-top': 5, 'enable_local_file_access': True}
    filename = 'deficiency-report.pdf'
    show_content_in_browser=True

    def get_object(self):
        report_obj = get_object_or_404(Questionaire, id=self.kwargs['pk'])
        return report_obj

    def get_recommended_product(self):
        product_recommendation_list = []
        obj = self.get_object()
        recommendation_data = obj.get_recommandation()
        for rec_item in recommendation_data.get('recommendation'):
            prod_obj_list = Product.objects.browsable().filter(title__startswith=rec_item)
            product_recommendation_list = product_recommendation_list + list(prod_obj_list)
        if len(product_recommendation_list) > 0:
            return product_recommendation_list[0]    
        return None      

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)    
        context['object'] = self.get_object()
        context['recommended_product'] = self.get_recommended_product()
        return context


# import pdb
class NewHomePageView(TemplateView):
    """
    new homepage view according to latest design
    """
    template_name = 'website/new_templates/homepage2.html'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['banner_image_object'] = BannerImages.objects.all().first()
        context['who_we_are'] = Who_we_are.objects.all().filter()
        context['blog'] = Blog.objects.all().filter(is_active = True)
        context['micronutreint'] = Micronutrientdeficiency.objects.all().filter(is_active = True)
        context['how_it_work'] = How_it_work.objects.all().filter(is_active = True)
        context['our_products'] = Our_products.objects.all().filter(is_active = True)
        context['consult'] = Consult.objects.all().filter(is_active = True)
        context['client_logo'] = Client_logo.objects.all().filter(is_active = True)
        context['faqicon'] = FaqIcon.objects.all().filter(is_active = True)
        context['header'] = Header.objects.all().filter(is_active = True)
 
        context['faqs_product'] = FAQSproduct.objects.all().filter(is_active = True)
        # context['question'] = Question.objects.all().filter(is_active = True)
        
        context['featured_product'] = Product.objects.filter(is_featured=True).filter(structure='parent')[:5]
        
        context['customer_testimonial_list'] = CustomerTestimonial.objects.filter(is_active=True)
        # context['category_with_product'] = self.get_product_with_category()
        # context['banner_img']=BannerImages.objects.get(is_active=True)
        context['dietitions_and_nutritionists'] = DietitionsAndNutritionists.objects.filter(dietitions_and_nutritionists='Dietitions')
        return context



class NewHeaderView(TemplateView):
    "new header view"
    template_name =  'website/new_templates/components/header.html'

    def get_context_data(self,*args, **kwargs):
        context = super(NewHeaderView, self).get_context_data(*args, **kwargs)
        context["header"] = Header.objects.all().filter(is_active = True)
        return context
         


class NewDetailView(ProductDetailView):
    """
    new homepage view according to latest design
    """
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    template_name = 'website/new_templates/detail_page.html'


class NewProductListView(ListView):
    """
    A view for display all the product in a website
    """
    model = Product
    template_name = 'website/new_templates/product_list.html'
    paginate_by = 10
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
                |Q(children__title__icontains=get_list)).distinct()
        
        
        
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
        context = super(NewProductListView, self).get_context_data(**kwargs)
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

class NewReviewView(ListView):
    """
    Review View
    """
    
    model = ProductReview
    template_name = 'website/new_templates/review.html'

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

class NewAboutUsView(TemplateView):
    """
    AboutUs View
    """

    template_name = 'website/new_templates/about-us.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NewAboutUsView, self).get_context_data(*args, **kwargs)
        
        context['frame1'] = Frame1.objects.filter(is_active=True)
        context['frame2'] = Frame2.objects.filter(is_active=True)
        context['frame3'] = Frame3.objects.filter(is_active=True)
        context['frame4'] = Frame4.objects.filter(is_active=True)
        context['frame5'] = Frame5.objects.filter(is_active=True)
        context['customer_testimonial_list'] = CustomerTestimonial.objects.filter(is_active=True)
      
        return context     



class NewContactUsView(SuccessMessageMixin, FormView):
    """
    ContactUs View
    """
    success_message = SUCCESS_MESSAGES['CONTACT_US_SUCCESS_MESSAGE']
    form_class = ContactUsForm
    template_name = 'website/new_templates/contact-us.html'
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

class NewFaqView(TemplateView):
    """
    Faq View
    """
    template_name = 'website/new_templates/faq.html'   
    def get_context_data(self, **kwargs):  
        context = super(self.__class__, self).get_context_data(**kwargs) 
        context["question"] = Question.objects.all().filter(is_active = True)
        context["faqicon"] = FaqIcon.objects.all().filter(is_active = True)
        context["consult"] = Consult.objects.all().filter(is_active = True)

        return context  


class NewPrivacyPolicyView(TemplateView):
    """
    PrivacyPolicy View
    """
    template_name = 'website/new_templates/privacy-policy.html'

class NewTermsOfUseView(TemplateView):
    """
    TermsOfUse View
    """
    template_name = 'website/new_templates/terms-of-use.html'


class NewReturnPolicyView(TemplateView):
    """
    ReturnPolicy View
    """
    template_name = 'website/new_templates/return_policy.html'


class NewShippingPolicyView(TemplateView):
    """
    ShippingPolicy View
    """
    template_name = 'website/new_templates/shipping_policy.html'



class NewProductDetailsView(ProductDetailView):
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
        context = super( NewProductDetailsView, self).get_context_data(*args, **kwargs)
        
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
        context['product_faqs'] = FAQSproduct.objects.filter(product=self.object).order_by('-question')

        return context 