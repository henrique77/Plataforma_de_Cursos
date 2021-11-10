from django.shortcuts import render, get_object_or_404

from .models import Course
from .forms import ContactCourse

def index(request):
    courses = Course.object.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

# def details(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     context = {
#         'course': course
#     }
#     template_name = 'courses/details.html'
#     return render(request, template_name, context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        form = ContactCourse(request.POST)
    else:
        form = ContactCourse()
    context = {
        'course': course,
        'form': form
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)