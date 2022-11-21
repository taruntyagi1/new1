from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

from catalogue.views import (
  AboutUsView,
  HomepageView,
  ContactUsView,
  PrivacyPolicyView,
  ReviewView,
  TermsOfUseView,
  ReturnPolicyView,
  ShippingPolicyView,
  FaqView,
  Who_we_areView,
  Who_we_areDetailView,
  ProductListView,
  ProductDetailsView,
  HeaderView



)
from website.views import (
  SitemapView, 
  DefficiencyAssessmentView, 
  DeffieicencyReportView,
  DeffieicencyReportPdfView,
  NewHomePageView,
  # DeffieicencyPdfReportPdfView,
  NewProductListView,
  NewReviewView,
  NewAboutUsView,NewContactUsView,
  NewFaqView,NewReturnPolicyView,NewTermsOfUseView, NewPrivacyPolicyView,NewShippingPolicyView,NewProductDetailsView,NewHeaderView
)

app_name = 'website'
urlpatterns = [
  path("old-page", HomepageView.as_view(), name='homepage'),
  path("about_us/", NewAboutUsView.as_view(), name='about_us'),  
  path("review/",  NewReviewView.as_view(), name='review'), 
  path("contact_us/", NewContactUsView.as_view(), name='contact_us'),  
  path("privacy_policy/", NewPrivacyPolicyView.as_view(), name='privacy_policy'),  
  path("terms_of_use/", NewTermsOfUseView.as_view(), name='terms_of_use'),  
  path("return_policy/",NewReturnPolicyView.as_view(), name='return_policy'),  
  path("shipping_policy/", NewShippingPolicyView.as_view(), name='shipping_policy'),  
  path("faq/", NewFaqView.as_view(), name='faq'),  
  path("who_we_are_list/", Who_we_areView.as_view(), name='blog_list'),  
  path("who_we_are_detail/", Who_we_areDetailView.as_view(), name='blog_detail'),  
  path("product/", NewProductListView.as_view(), name='product_list'),  
  # path("product/<slug:slug>", ProductDetailsView.as_view(), name='product_detail'), 
  path("product-new/<slug:slug>", NewProductDetailsView.as_view(), name='product_detail'), 
  path("defficiency-assessment", DefficiencyAssessmentView.as_view(), name='defficiency_assessment'),
  path("defficiency-report/<int:pk>/", DeffieicencyReportView.as_view(), name='defficiency_report'),
  path("defficiency-report/<int:pk>/pdf", DeffieicencyReportPdfView.as_view(), name='defficiency_report_pdf'),
  # path("defficiency-report/<int:pk>/view",  DeffieicencyPdfReportPdfView.as_view(), name='defficiency_report_pdf_view'),
  path("", NewHomePageView.as_view(), name='new_homepage'),
   path("header_list/", HeaderView.as_view(), name='header'),  
  url('sitemap.xml/',TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
  url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')), 
]
