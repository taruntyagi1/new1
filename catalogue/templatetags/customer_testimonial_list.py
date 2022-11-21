from django import template
from catalogue.models import CustomerTestimonial

register = template.Library()

@register.simple_tag
def get_customer_testimonial():
    return CustomerTestimonial.objects.filter(is_active=True)