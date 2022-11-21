# basic context processors

# local imports
from catalogue.models import (
    Category,
    Product,
)

def get_level_one_category(request):
    category_list = Category.objects.filter(depth=1, is_active=True)
    if category_list.exists():
        return {'level_1_category': category_list}
    return {'level_1_category': None}

def get_footer_gallery_products(request):
    gallery_list = Product.objects.filter(is_active=True, is_add_to_gallery=True)[:6]
    if gallery_list.exists():
        return {'footer_gallery': gallery_list}
    return {'footer_gallery': None}
