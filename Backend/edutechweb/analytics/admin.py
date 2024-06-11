# Register your models here.
from django.contrib import admin
from .models import CourseAnalytics

@admin.register(CourseAnalytics)
class CourseAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('course', 'enrollment_count', 'completion_rate', 'total_revenue')
    list_filter = ('course',)
    search_fields = ('course__title',)
