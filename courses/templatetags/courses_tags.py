#from django.template import Library
from django import template

register = template.Library()

from courses.models import Enrollment

@register.simple_tag
def load_my_courses(user):
    return Enrollment.objects.filter(user=user)