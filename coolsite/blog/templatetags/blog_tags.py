from django import template
from blog.models import *

register = template.Library()

@register.simple_tag(name = "categories")
def get_categories(filters = None):
    if not filters:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filters)

@register.inclusion_tag('blog/show_category.html')
def get_show_categories(sort=None,cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    context = {
    'cats':cats,
    }
    return context
