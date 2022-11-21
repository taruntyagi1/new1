# django imports
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.urls import reverse_lazy
from django.db import models
from django.contrib import messages
from django.http import HttpResponseRedirect

# oscar imports
from oscar.apps.dashboard.catalogue.views import (
    ProductCreateUpdateView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryListView,
    ProductClassCreateView,
    ProductClassUpdateView,
    ProductClassListView,
    ProductListView,


    
    
)

# inner app imports
from catalogue.models import (

    BannerImages,
    Who_we_are,
    DietitionsAndNutritionists,
    Product,
    NewsLetter,
    CustomerTestimonial,
    ProductReview,
    Questionaire,
    Micronutrientdeficiency,
    How_it_work,
    Our_products,
    Consult,
    Client_logo,
    Blog,
    FAQSproduct,
    Question,
    FaqIcon,
    Frame1,
    Frame2,
    Frame3,
    Frame4,
    Frame5,
    Header,
    Footer

    
    
    
    
    
    
)
from canleath.messages import (
    SUCCESS_MESSAGES,
    ERROR_MESSAGES,
)

# local imports
from .forms import (
    DietitionsAndNutritionistsForm,
    Who_we_areForm,
    ProductForm,
    CategoryForm,
    BannerImageForm,
    ProductClassForm,
    ProductReviewForm,
    BlogForm,
    MicronutrientdeficiencyForm,
    How_it_workForm,
    Our_productsForm,
    ConsultForm,
    Client_logoForm,
    BlogForm,
    FAQSproductForm,
    QuestionForm,
    FaqIconForm,
    Frame1Form,
    Frame2Form,
    Frame3Form,
    Frame4Form,
    Frame5Form,
    HeaderForm,
    FooterForm
   
)
from .formset import CustomStockRecordFormSet

from .tables import (
    CategoryTable,
    ProductTable,
)

class ProductCreateOrUpdateView(ProductCreateUpdateView):
    """
    View for create or update product
    """

    form_class = ProductForm
    stockrecord_formset = CustomStockRecordFormSet
    template_name = 'catalogue/product_update.html'


class CustomProductListView(ProductListView):
    """
    Custom Product List View
    """

    table_class = ProductTable


class CategoriesCreateView(CategoryCreateView):
    """
    View for create category
    """

    form_class = CategoryForm
    template_name = 'catalogue/category_form.html'


class CategoriesUpdateView(CategoryUpdateView):
    """
    View for update category
    """

    form_class = CategoryForm
    template_name = 'catalogue/category_form.html'


class CategoriesListView(CategoryListView):
    """
    Category List View
    """
    table_class = CategoryTable


class BannerImagesListView(ListView):
    """
    List View for Banner Images
    """

    model = BannerImages
    raise_exception = True
    success_url = reverse_lazy('dashboard:banner_image_list')
    paginate_by = 20

    def get_success_url(self):
        return reverse_lazy('dashboard:banner_image_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class BannerImageCreateView(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/banner_images_form.html'
    model = BannerImages
    form_class = BannerImageForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:banner_image_list')


class BannerImageUpdateView(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/banner_images_form.html'
    model = BannerImages
    raise_exception = True
    fields = (
        'image',
        'title',
        'subtitle',
        'hyperlink',
        'is_active',
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:banner_image_list')


class CustomProductClassCreateView(ProductClassCreateView):
    """
    Custom Product Class Create View
    """

    form_class = ProductClassForm


class CustomProductClassUpdateView(ProductClassUpdateView):
    """
    Custom Product Class Update View
    """

    form_class = ProductClassForm


class CustomProductClassListView(ProductClassListView):
    """
    Custom Product Class List View
    """

    template_name = 'catalogue/product_class_list.html'


class NewsLetterListView(ListView):
    """
    List View for Banner Images
    """

    model = NewsLetter
    raise_exception = True
    success_url = reverse_lazy('dashboard:news_letter_list')
    paginate_by = 20

    def get_success_url(self):
        return reverse_lazy('dashboard:news_letter_list')

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('news_letter')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class CustomerTestimonialListView(ListView):
    """
    List View for Banner Images
    """

    model = CustomerTestimonial
    raise_exception = True
    success_url = reverse_lazy('dashboard:customer_testimonial_list')
    paginate_by = 20
    template_name = 'catalogue/customer_testimonial_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:customer_testimonial_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('testimonial')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class CustomerTestimonialCreateView(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/customer_testimonial_form.html'
    model = CustomerTestimonial
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        'product',
        'name',
        'customer_image',
        'review',
        'city',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:customer_testimonial_list')


class CustomerTestimonialUpdateView(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/customer_testimonial_form.html'
    model = CustomerTestimonial
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        'product',
        'name',
        'customer_image',
        'review',
        'city',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:customer_testimonial_list')



class DietitionsAndNutritionistsListView(ListView):
    """
    List View for DietitionsAndNutritionists
    """
    
    model = DietitionsAndNutritionists
    raise_exception = True
    template_name = 'catalogue/dietitions_and_nutritionists_list.html'
    success_url = reverse_lazy('dashboard:dietitions_and_nutritionists_list')
    paginate_by = 20

    def get_success_url(self):
        return reverse_lazy('dashboard:dietitions_and_nutritionists_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class DietitionsAndNutritionistsCreateView(CreateView):
    """
    DietitionsAndNutritionists Create View
    """

    template_name = 'catalogue/dietitions_and_nutritionists_form.html'
    model = DietitionsAndNutritionists
    form_class = DietitionsAndNutritionistsForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:dietitions_and_nutritionists_list')


class DietitionsAndNutritionistsUpdateView(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/dietitions_and_nutritionists_form.html'
    model = DietitionsAndNutritionists
    raise_exception = True
    form_class = DietitionsAndNutritionistsForm

    # fields = (
    #     'product',
    #     'title',
    #     'description',
    #     'image',
    #     'url',
    #     'dietitions_and_nutritionists'
    # )

    success_message = SUCCESS_MESSAGES['DIETITIANS_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:dietitions_and_nutritionists_list')





class Who_we_areCreateView(CreateView):
    """
    Blog Create View
    """

    template_name = 'catalogue/who_we_are_form.html'
    model = Who_we_are
    form_class = Who_we_areForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:who_we_are_list')


class Who_we_areUpdateView(UpdateView):
    
    template_name = 'catalogue/who_we_are_form.html'
    model = Who_we_are
    raise_exception = True
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

    success_message = SUCCESS_MESSAGES['BLOG_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:who_we_are_list')


class Who_we_areListView(ListView):
    """
    List View for Who_we_are
    """
    
    model = Who_we_are
    raise_exception = True
    template_name = 'catalogue/who_we_are_list.html'
    success_url = reverse_lazy('dashboard:who_we_are_list')
    paginate_by = 20

    def get_success_url(self):
        return reverse_lazy('dashboard:who_we_are_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class ProductReviewListView(ListView):
    """
    List View for ProductReview
    """

    model = ProductReview
    raise_exception = True
    template_name = 'catalogue/product_review_list.html'
    success_url = reverse_lazy('dashboard:product_review_list')
    paginate_by = 20

    def get_success_url(self):
        return reverse_lazy('dashboard:product_review_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('reviews')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())

class ProductReviewCreateView(CreateView):
    """
   ProductReview Create View
    """
   

    template_name = 'catalogue/product_review_form.html'
    model = ProductReview
    form_class = ProductReviewForm

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(self.__class__, self).get_form_kwargs(*args, **kwargs)
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:product_review_list')


class ProductReviewUpdateView(UpdateView):
    """
    View for Update Product review
    """

    template_name = 'catalogue/product_review_form.html'
    model = ProductReview
    raise_exception = True
    form_class = ProductReviewForm
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(self.__class__, self).get_form_kwargs(*args, **kwargs)
        kwargs['request'] = self.request
        return kwargs
    # fields = (
    #     'review',
    #     'product',
    #     'rating',
    #     'user',
    #     'video_url',
    #     'is_approved',
    #     'is_featured',
    # )

    success_message = SUCCESS_MESSAGES['PRODUCT_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:product_review_list')



class FAQSproductListView(ListView):
    """
    List View for FAQS
    """

    model = FAQSproduct
    raise_exception = True
    template_name = 'catalogue/faqsproduct_list.html'
    success_url = reverse_lazy('dashboard:faqsproduct_list')
    paginate_by = 20

    def get_success_url(self):
        return reverse_lazy('dashboard:faqsproduct_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('faqs')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class FAQSproductCreateView(CreateView):
    """
    FAQS Create View
    """

    template_name = 'catalogue/faqsproduct_form.html'
    model = FAQSproduct
    form_class = FAQSproductForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:faqsproduct_list')

class FAQSproductUpdateView(UpdateView):
    """
    View for Update FAQS
    """

    template_name = 'catalogue/faqsproduct_form.html'
    model = FAQSproduct
    raise_exception = True
    form_class = FAQSproductForm
   
    success_message = SUCCESS_MESSAGES['PRODUCT_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:faqsproduct_list')



class BlogListView(ListView):
   
    model = Blog
    raise_exception = True
    template_name = 'catalogue/blog_list.html'
    success_url = reverse_lazy('dashboard:blog_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:blog_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class BlogCreateView(CreateView):
    """
   blog Create View
    """
    template_name = 'catalogue/blog_form.html'
    model = Blog
    form_class: BlogForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        'main_heading',
        'title',
        'description',
        'image',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:blog_list')

class BlogUpdateView(UpdateView):
   
    template_name = 'catalogue/blog_form.html'
    model = Blog
    form_class: BlogForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        'main_heading',
        'title',
        'description',
        'image',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:blog_list')





class MicronutrientdeficiencyListView(ListView):
   
    model = Micronutrientdeficiency
    raise_exception = True
    template_name = 'catalogue/micronutrient_list.html'
    success_url = reverse_lazy('dashboard:micronutrient_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:micronutrient_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class MicronutrientdeficiencyCreateView(CreateView):
    """
   Micronutrientdeficiency Review Create View
    """
    template_name = 'catalogue/micronutrient_form.html'
    model = Micronutrientdeficiency
    form_class: MicronutrientdeficiencyForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
    
        'heading',
        'description',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:micronutrient_list')

class MicronutrientdeficiencyUpdateView(UpdateView):
   
    template_name = 'catalogue/micronutrient_form.html'
    model = Micronutrientdeficiency
    form_class: MicronutrientdeficiencyForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
     
        'heading',
        'description',
    
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:micronutrient_list')



class Our_productsListView(ListView):
   
    model = Our_products
    raise_exception = True
    template_name = 'catalogue/our_products_list.html'
    success_url = reverse_lazy('dashboard:our_products_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:our_products_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class Our_productsCreateView(CreateView):
    """
   Our_products Create View
    """
    template_name = 'catalogue/our_products_form.html'
    model = Our_products
    form_class: Our_productsForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
    
        'title',
        'image',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:our_products_list')

class Our_productsUpdateView(UpdateView):
   
    template_name = 'catalogue/our_products_form.html'
    model = Our_products
    form_class: Our_productsForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
     
        'title',
        'image',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:our_products_list')




class How_it_workListView(ListView):
   
    model = How_it_work
    raise_exception = True
    template_name = 'catalogue/How_it_work_list.html'
    success_url = reverse_lazy('dashboard:how_it_work_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:how_it_work_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class How_it_workCreateView(CreateView):
    """
   SectionReview Create View
    """
    template_name = 'catalogue/how_it_work_form.html'
    model = How_it_work
    form_class: How_it_workForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        
       'main_title',
        'title',
        'description',
        'title2',
        'description2',
        'title3',
        'description3',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:how_it_work_list')

class How_it_workUpdateView(UpdateView):
   
    template_name = 'catalogue/how_it_work_form.html'
    model = How_it_work
    form_class: How_it_workForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        
        'main_title',
        'title',
        'description',
        'title2',
        'description2',
        'title3',
        'description3',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:how_it_work_list')

   





class QuestionaireListView(ListView):
    """
    List View for Questionaire
    """

    model = Questionaire
    raise_exception = True
    template_name = 'catalogue/questionaire_list.html'
    success_url = reverse_lazy('dashboard:questionaire_list')
    paginate_by = 20

    def get_success_url(self):
        return reverse_lazy('dashboard:questionaire_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().order_by('-id')
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('questionaire')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class ConsultListView(ListView):
   
    model = Consult
    raise_exception = True
    template_name = 'catalogue/consult_list.html'
    success_url = reverse_lazy('dashboard:consult_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:consult_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class ConsultCreateView(CreateView):
    """
   SectionReview Create View
    """
    template_name = 'catalogue/consult_form.html'
    model = Consult
    form_class: ConsultForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        'title',
        'button',
        'image',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:consult_list')

class ConsultUpdateView(UpdateView):
   
    template_name = 'catalogue/consult_form.html'
    model = Consult
    form_class: ConsultForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        'title',
        'button',
        'image',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:consult_list')




class Client_logoListView(ListView):
   
    model = Client_logo
    raise_exception = True
    template_name = 'catalogue/client_logo_list.html'
    success_url = reverse_lazy('dashboard:client_logo_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:client_logo_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class Client_logoCreateView(CreateView):
    """
   client_logo Create View
    """
    template_name = 'catalogue/client_logo_form.html'
    model = Client_logo
    form_class: Client_logoForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        'image',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:client_logo_list')

class Client_logoUpdateView(UpdateView):
   
    template_name = 'catalogue/client_logo_form.html'
    model = Client_logo
    form_class: Client_logoForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        'image',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:client_logo_list')




class QuestionListView(ListView):
   
    model = Question
    raise_exception = True
    template_name = 'catalogue/question_list.html'
    success_url = reverse_lazy('dashboard:question_list')
    paginate_by = 10
    
    def get_success_url(self):
        return reverse_lazy('dashboard:question_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset
    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('question')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class QuestionCreateView(CreateView):
    """
   Question Create View
    """
    template_name = 'catalogue/question_form.html'
    model = Question
    form_class: QuestionForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        'question',
        'answer',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:question_list')

class QuestionUpdateView(UpdateView):
   
    template_name = 'catalogue/question_form.html'
    model = Question
    form_class: QuestionForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        'question',
        'answer',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:question_list')








class Frame1ListView(ListView):
   
    model = Frame1
    raise_exception = True
    template_name = 'catalogue/frame1_list.html'
    success_url = reverse_lazy('dashboard:frame1_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:frame1_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset
    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().order_by('id')
        return queryset



    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class Frame1CreateView(CreateView):
    """
   Question Create View
    """
    template_name = 'catalogue/frame1_form.html'
    model = Frame1
    form_class: Frame1Form
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        'frames',
        'image',
        'title',
        'description',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:frame1_list')


  

class Frame1UpdateView(UpdateView):
   
    template_name = 'catalogue/frame1_form.html'
    model = Frame1
    form_class: Frame1Form
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        'frames',
        'image',
        'title',
        'description',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:frame1_list')




class FaqIconListView(ListView):
   
    model = FaqIcon
    raise_exception = True
    template_name = 'catalogue/faqicon_list.html'
    success_url = reverse_lazy('dashboard:faqicon_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:faqicon_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset
    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class FaqIconCreateView(CreateView):
    """
   Question Create View
    """
    template_name = 'catalogue/faqicon_form.html'
    model = FaqIcon
    form_class: FaqIconForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        'image',
        'step',
        'title',
        'description',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:faqicon_list')

class FaqIconUpdateView(UpdateView):
   
    template_name = 'catalogue/faqicon_form.html'
    model = FaqIcon
    form_class: FaqIconForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        'image',
        'step',
        'title',
        'description',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:faqicon_list')


class Frame2ListView(ListView):
   
    model = Frame2
    raise_exception = True
    template_name = 'catalogue/frame2_list.html'
    success_url = reverse_lazy('dashboard:frame2_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:frame2_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset
    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class Frame2CreateView(CreateView):
    """
   Question Create View
    """
    template_name = 'catalogue/frame2_form.html'
    model = Frame2
    form_class: Frame2Form
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        'image',
        'title',
        'description',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:frame2_list')

class Frame2UpdateView(UpdateView):
   
    template_name = 'catalogue/frame2_form.html'
    model = Frame2
    form_class: Frame2Form
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        'image',
        'title',
        'description',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:frame2_list')


class Frame3ListView(ListView):
   
    model = Frame3
    raise_exception = True
    template_name = 'catalogue/frame3_list.html'
    success_url = reverse_lazy('dashboard:frame3_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:frame3_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset
    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class Frame3CreateView(CreateView):
    """
   Question Create View
    """
    template_name = 'catalogue/frame3_form.html'
    model = Frame3
    form_class: Frame3Form
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        'image',
        'title',
        'description',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:frame3_list')

class Frame3UpdateView(UpdateView):
   
    template_name = 'catalogue/frame3_form.html'
    model = Frame3
    form_class: Frame3Form
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        'image',
        'title',
        'description',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:frame3_list')


class Frame4ListView(ListView):
   
    model = Frame4
    raise_exception = True
    template_name = 'catalogue/frame4_list.html'
    success_url = reverse_lazy('dashboard:frame4_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:frame4_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset
    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class Frame4CreateView(CreateView):
    """
   Question Create View
    """
    template_name = 'catalogue/frame4_form.html'
    model = Frame4
    form_class: Frame1Form
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
        'image',
        'title',
        'description1',
        'description2',
        'description3',
        'description4',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:frame4_list')

class Frame4UpdateView(UpdateView):
   
    template_name = 'catalogue/frame4_form.html'
    model = Frame4
    form_class: Frame4Form
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
        'image',
        'title',
        'description1',
        'description2',
        'description3',
        'description4',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:frame4_list')



class Frame5ListView(ListView):
   
    model = Frame5
    raise_exception = True
    template_name = 'catalogue/frame5_list.html'
    success_url = reverse_lazy('dashboard:frame5_list')
    paginate_by = 20
    
    def get_success_url(self):
        return reverse_lazy('dashboard:frame5_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset
    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class Frame5CreateView(CreateView):
    """
   Question Create View
    """
    template_name = 'catalogue/frame5_form.html'
    model = Frame5
    form_class: Frame5Form
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
       
        'title',
        'description',
        'choice',
        'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:frame5_list')

class Frame5UpdateView(UpdateView):
   
    template_name = 'catalogue/frame5_form.html'
    model = Frame5
    form_class: Frame5Form
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
       'title',
        'description',
       'choice',
        'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:frame5_list')






class HeaderListView(ListView):
   
    model = Header
    raise_exception = True
    template_name = 'catalogue/header_list.html'
    success_url = reverse_lazy('dashboard:header_list')
    paginate_by = 10
    
    def get_success_url(self):
        return reverse_lazy('dashboard:header_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset
    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class HeaderCreateView(CreateView):
    """
   Question Create View
    """
    template_name = 'catalogue/header_form.html'
    model = Header
    form_class: HeaderForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
       
       'image',
       'title',
       'hyperlink',
       'icon',
       'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:header_list')

class HeaderUpdateView(UpdateView):
   
    template_name = 'catalogue/header_form.html'
    model = Header
    form_class: HeaderForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
       'image',
       'title',
       'hyperlink',
       'icon',
       'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:header_list')




class FooterListView(ListView):
   
    model = Footer
    raise_exception = True
    template_name = 'catalogue/footer_list.html'
    success_url = reverse_lazy('dashboard:footer_list')
    paginate_by = 10
    
    def get_success_url(self):
        return reverse_lazy('dashboard:footer_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        return queryset
    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())




class FooterCreateView(CreateView):
    """
   Question Create View
    """
    template_name = 'catalogue/footer_form.html'
    model = Footer
    form_class: FooterForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_ADDED']

    fields = (
       
       'image',
       'footer',
       'title',
       'links',
       'icon',
       'hyperlink',
       'is_active',
    )

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:footer_list')

class FooterUpdateView(UpdateView):
   
    template_name = 'catalogue/footer_form.html'
    model = Footer
    form_class: FooterForm
    raise_exception = True
    success_message = SUCCESS_MESSAGES['CUSTOMER_TESTIMONIAL_UPDATE']

    fields = (
       'image',
       'footer',
       'title',
       'links',
       'icon',
       'hyperlink',
       'is_active',
    )

    def get_success_url(self):
        return reverse_lazy('dashboard:footer_list')




