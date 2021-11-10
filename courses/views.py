from django.shortcuts import render

from .models import Course

def index(request):
    courses = Course.object.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)
