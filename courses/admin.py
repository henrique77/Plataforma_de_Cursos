from django.contrib import admin

from .models import Course

#Customizar o model no admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)
