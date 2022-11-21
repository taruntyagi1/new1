from django import template
import ipdb
register = template.Library()

@register.simple_tag
def go_to_cart_product(request, product):
    
    # if isinstance(product,str):
    #     dic={'status':False}
    #     return dic
    if product.structure == 'child':
        product = product.parent
    for line in request:
        if line.product.structure == 'child':
            line_product = line.product.parent
        else:
            line_product = line.product    
        if product.id == line_product.id:
            dic={'line':line, 'basket_product':line.product.title,'status':True}
            return dic
    dic={'status':False}
    return dic
  