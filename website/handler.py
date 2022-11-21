from re import template
from django.http import request
from django.shortcuts import render

def page_not_found_view(request, exception=None):
    context = {}
    template_name = '404.html'
    response = render(request, template_name, context=context)
    response.status_code = 404
    return response