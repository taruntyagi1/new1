# oscar imports
import oscar.apps.dashboard.catalogue.apps as apps
from oscar.core.loading import get_class
from django.conf.urls import url


#local imports

class CatalogueDashboardConfig(apps.CatalogueDashboardConfig):
    name = 'dashboard.catalogue'

    def ready(self):
        super(CatalogueDashboardConfig, self).ready()
        from .views import (
            ProductCreateOrUpdateView,
            CategoriesCreateView,
            CategoriesUpdateView,
            BannerImagesListView,
            BannerImageCreateView,
            BannerImageUpdateView,
            CategoriesListView,
            CustomProductClassCreateView,
            CustomProductClassUpdateView,
            CustomProductClassListView,
            CustomProductListView,
            NewsLetterListView,
            CustomerTestimonialCreateView,
            CustomerTestimonialUpdateView,
            CustomerTestimonialListView,
            DietitionsAndNutritionistsCreateView,
            DietitionsAndNutritionistsListView,
            DietitionsAndNutritionistsUpdateView,
            Who_we_areCreateView,
            Who_we_areListView, 
            Who_we_areUpdateView,
            ProductReviewListView,
            ProductReviewCreateView,
            ProductReviewUpdateView,
            FAQSproductListView,
            FAQSproductCreateView,
            FAQSproductUpdateView,
            QuestionaireListView,
            BlogListView,
            BlogCreateView,
            BlogUpdateView,
            MicronutrientdeficiencyCreateView,
            MicronutrientdeficiencyListView,
            MicronutrientdeficiencyUpdateView,
            How_it_workListView,
            How_it_workCreateView,
            How_it_workUpdateView,
            Our_productsListView,
            Our_productsCreateView,
            Our_productsUpdateView,
            ConsultListView,
            ConsultCreateView,
            ConsultUpdateView,
            Client_logoListView,
            Client_logoCreateView,
            Client_logoUpdateView,
            QuestionListView,
            QuestionCreateView,
            QuestionUpdateView,
            FaqIconListView,
            FaqIconCreateView,
            FaqIconUpdateView,
            Frame1ListView,
            Frame1CreateView,
            Frame1UpdateView,
            Frame2ListView,
            Frame2CreateView,
            Frame2UpdateView,
            Frame3ListView,
            Frame3CreateView,
            Frame3UpdateView,
            Frame4ListView,
            Frame4CreateView,
            Frame4UpdateView,
            Frame5ListView,
            Frame5CreateView,
            Frame5UpdateView,
            HeaderListView,
            HeaderCreateView,
            HeaderUpdateView,
            FooterCreateView,
            FooterListView,
            FooterUpdateView
          


        )
        self.product_createupdate_view = ProductCreateOrUpdateView
        self.category_create_view = CategoriesCreateView
        self.category_update_view = CategoriesUpdateView
        self.banner_image_list_view = BannerImagesListView
        self.banner_image_create_view = BannerImageCreateView
        self.banner_image_update_view = BannerImageUpdateView
        self.category_list_view = CategoriesListView
        self.product_class_create_view = CustomProductClassCreateView
        self.product_class_update_view = CustomProductClassUpdateView
        self.product_class_list_view = CustomProductClassListView
        self.product_list_view = CustomProductListView
        self.news_letter_list = NewsLetterListView
        self.customer_testimonial_list_view = CustomerTestimonialListView
        self.customer_testimonial_create_view = CustomerTestimonialCreateView
        self.customer_testimonial_update_view = CustomerTestimonialUpdateView
        self.dietitions_and_nutritionists_list_view = DietitionsAndNutritionistsListView
        self.dietitions_and_nutritionists_create_view = DietitionsAndNutritionistsCreateView
        self.dietitions_and_nutritionists_update_view = DietitionsAndNutritionistsUpdateView
        self.who_we_are_list_view = Who_we_areListView
        self.who_we_are_create_view = Who_we_areCreateView
        self.who_we_are_update_view = Who_we_areUpdateView
        self.product_review_list_view = ProductReviewListView
        self.product_review_create_view = ProductReviewCreateView
        self.product_review_update_view = ProductReviewUpdateView
        self.faqsproduct_list_view = FAQSproductListView
        self.faqsproduct_create_view = FAQSproductCreateView
        self.faqsproduct_update_view = FAQSproductUpdateView
        self.questionaire_list_view = QuestionaireListView
        self.blog_list_view = BlogListView
        self.blog_create_view = BlogCreateView
        self.blog_update_view = BlogUpdateView
        self.micronutrient_create_view = MicronutrientdeficiencyCreateView
        self.micronutrient_list_view = MicronutrientdeficiencyListView
        self.micronutrient_update_view = MicronutrientdeficiencyUpdateView
        self.how_it_work_create_view = How_it_workCreateView
        self.how_it_work_list_view = How_it_workListView
        self.how_it_work_update_view = How_it_workUpdateView
        self.our_products_create_view = Our_productsCreateView
        self.our_products_list_view = Our_productsListView
        self.our_products_update_view = Our_productsUpdateView
        self.consult_list_view = ConsultListView
        self.consult_create_view = ConsultCreateView
        self.consult_update_view = ConsultUpdateView
        self.client_logo_list_view =  Client_logoListView
        self.client_logo_create_view =  Client_logoCreateView
        self.client_logo_update_view =  Client_logoUpdateView
        self.question_list_view = QuestionListView
        self.question_create_view = QuestionCreateView
        self.question_update_view = QuestionUpdateView
        self.faqicon_update_view =  FaqIconUpdateView
        self.faqicon_list_view =  FaqIconListView
        self.faqicon_create_view =  FaqIconCreateView
        self.frame1_list_view = Frame1ListView
        self.frame1_create_view = Frame1CreateView
        self.frame1_update_view = Frame1UpdateView
        self.frame2_list_view = Frame2ListView
        self.frame2_create_view = Frame2CreateView
        self.frame2_update_view = Frame2UpdateView
        self.frame3_list_view = Frame3ListView
        self.frame3_create_view = Frame3CreateView
        self.frame3_update_view = Frame3UpdateView
        self.frame4_list_view = Frame4ListView
        self.frame4_create_view = Frame4CreateView
        self.frame4_update_view = Frame4UpdateView
        self.frame5_list_view = Frame5ListView
        self.frame5_create_view = Frame5CreateView
        self.frame5_update_view = Frame5UpdateView
        self.header_list_view = HeaderListView
        self.header_create_view = HeaderCreateView
        self.header_update_view = HeaderUpdateView
        self.footer_create_view = FooterCreateView
        self.footer_list_view = FooterListView
        self.footer_update_view = FooterUpdateView
        
        
        
        
       

    def get_urls(self):
        urls = super(CatalogueDashboardConfig, self).get_urls()
        urls += [
            url(r'^banner_images/$', self.banner_image_list_view.as_view(), name='banner_image_list'),
            url(r'^banner_images/create/$', self.banner_image_create_view.as_view(), name='banner_image_create'),
            url(r'^banner_images/(?P<pk>\d+)/update/$', self.banner_image_update_view.as_view(), name='banner_image_update'),
            url(r'^news_letter/$', self.news_letter_list.as_view(), name='news_letter_list'),
            url(r'^customer_testimonial/$', self.customer_testimonial_list_view.as_view(), name='customer_testimonial_list'),
            url(r'^customer_testimonial/create/$', self.customer_testimonial_create_view.as_view(), name='customer_testimonial_create'),
            url(r'^customer_testimonial/(?P<pk>\d+)/update/$', self.customer_testimonial_update_view.as_view(), name='customer_testimonial_update'),
            url(r'^dietitions_and_nutritionists/list/$', self.dietitions_and_nutritionists_list_view.as_view(), name='dietitions_and_nutritionists_list'),
            url(r'^dietitions_and_nutritionists/create/$', self.dietitions_and_nutritionists_create_view.as_view(), name='dietitions_and_nutritionists_create'),
            url(r'^dietitions_and_nutritionists/(?P<pk>\d+)/update/$', self.dietitions_and_nutritionists_update_view.as_view(), name='dietitions_and_nutritionists_update'),
            url(r'^who_we_are/list/$', self.who_we_are_list_view.as_view(), name='who_we_are_list'),
            url(r'^who_we_are/create/$', self.who_we_are_create_view.as_view(), name='who_we_are_create'),
            url(r'^who_we_are/(?P<pk>\d+)/update/$', self.who_we_are_update_view.as_view(), name='who_we_are_update'),
            url(r'^product_review/list/$', self.product_review_list_view.as_view(), name='product_review_list'),
            url(r'^product_review/create/$', self.product_review_create_view.as_view(), name='product_review_create'),
            url(r'^product_review/(?P<pk>\d+)/update/$', self.product_review_update_view.as_view(), name='product_review_update'),
            url(r'^faqsproduct/list/$', self.faqsproduct_list_view.as_view(), name='faqsproduct_list'),
            url(r'^faqsproduct/create/$', self.faqsproduct_create_view.as_view(), name='faqsproduct_create'),
            url(r'^faqsproduct/(?P<pk>\d+)/update/$', self.faqsproduct_update_view.as_view(), name='faqsproduct_update'),
            url(r'^questionaire/list$', self.questionaire_list_view.as_view(), name='questionaire_list'),
            url(r'^blog/list$', self.blog_list_view.as_view(), name='blog_list'),
            url(r'^blog/create$', self.blog_create_view.as_view(), name='blog_create'),
            url(r'^blog/(?P<pk>\d+)/update$', self.blog_update_view.as_view(), name='blog_update'),
            url(r'^micronutrient/list$', self.micronutrient_list_view.as_view(), name='micronutrient_list'),
            url(r'^micronutrient/create$', self.micronutrient_create_view.as_view(), name='micronutrient_create'),
            url(r'^micronutrient/(?P<pk>\d+)/update$', self.micronutrient_update_view.as_view(), name='micronutrient_update'),
            url(r'^how_it_work/list$', self.how_it_work_list_view.as_view(), name='how_it_work_list'),
            url(r'^how_it_work/create$', self.how_it_work_create_view.as_view(), name='how_it_work_create'),
            url(r'^how_it_work/(?P<pk>\d+)/update$', self.how_it_work_update_view.as_view(), name='how_it_work_update'),
            url(r'^our_products/list$', self.our_products_list_view.as_view(), name='our_products_list'),
            url(r'^our_products/create$', self.our_products_create_view.as_view(), name='our_products_create'),
            url(r'^our_products/(?P<pk>\d+)/update$', self.our_products_update_view.as_view(), name='our_products_update'),
            url(r'^consult/list$', self.consult_list_view.as_view(), name='consult_list'),
            url(r'^consult/create$', self.consult_create_view.as_view(), name='consult_create'),
            url(r'^consult/(?P<pk>\d+)/update$', self.consult_update_view.as_view(), name='consult_update'),
            url(r'^client_logo/list$', self.client_logo_list_view.as_view(), name='client_logo_list'),
            url(r'^client_logo/create$', self.client_logo_create_view.as_view(), name='client_logo_create'),
            url(r'^client_logo/(?P<pk>\d+)/update$', self.client_logo_update_view.as_view(), name='client_logo_update'),
            url(r'^question/list/$', self.question_list_view.as_view(), name='question_list'),
            url(r'^question/create/$', self.question_create_view.as_view(), name='question_create'),
            url(r'^question/(?P<pk>\d+)/update/$', self.question_update_view.as_view(), name='question_update'),
            url(r'^faqicon/list/$', self.faqicon_list_view.as_view(), name='faqicon_list'),
            url(r'^faqicon/create/$', self.faqicon_create_view.as_view(), name='faqicon_create'),
            url(r'^faqicon/(?P<pk>\d+)/update/$', self.faqicon_update_view.as_view(), name='faqicon_update'),
            url(r'^frame1/list/$', self.frame1_list_view.as_view(), name='frame1_list'),
            url(r'^frame1/create/$', self.frame1_create_view.as_view(), name='frame1_create'),
            url(r'^frame1/(?P<pk>\d+)/update/$', self.frame1_update_view.as_view(), name='frame1_update'),
            url(r'^frame2/list/$', self.frame2_list_view.as_view(), name='frame2_list'),
            url(r'^frame2/create/$', self.frame2_create_view.as_view(), name='frame2_create'),
            url(r'^frame2/(?P<pk>\d+)/update/$', self.frame2_update_view.as_view(), name='frame2_update'),
            url(r'^frame3/list/$', self.frame3_list_view.as_view(), name='frame3_list'),
            url(r'^frame3/create/$', self.frame3_create_view.as_view(), name='frame3_create'),
            url(r'^frame3/(?P<pk>\d+)/update/$', self.frame3_update_view.as_view(), name='frame3_update'),
            url(r'^frame4/list/$', self.frame4_list_view.as_view(), name='frame4_list'),
            url(r'^frame4/create/$', self.frame4_create_view.as_view(), name='frame4_create'),
            url(r'^frame4/(?P<pk>\d+)/update/$', self.frame4_update_view.as_view(), name='frame4_update'),
            url(r'^frame5/list/$', self.frame5_list_view.as_view(), name='frame5_list'),
            url(r'^frame5/create/$', self.frame5_create_view.as_view(), name='frame5_create'),
            url(r'^frame5/(?P<pk>\d+)/update/$', self.frame5_update_view.as_view(), name='frame5_update'),
            url(r'^header/list/$', self.header_list_view.as_view(), name='header_list'),
            url(r'^header/create/$', self.header_create_view.as_view(), name='header_create'),
            url(r'^header/(?P<pk>\d+)/update/$', self.header_update_view.as_view(), name='header_update'),
            url(r'^footer/list/$', self.footer_list_view.as_view(), name='footer_list'),
            url(r'^footer/create/$', self.footer_create_view.as_view(), name='footer_create'),
            url(r'^footer/(?P<pk>\d+)/update/$', self.footer_update_view.as_view(), name='footer_update'),
            
            
        ]
        return self.post_process_urls(urls)