from ..models import Home
from django import template

register = template.Library()

@register.simple_tag
def Home_model(title):
    return Home.objects.filter(title=title).first().description