from rest_framework import serializers
from .models import CourseAnalytics

class CourseAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAnalytics
        fields = ('course', 'enrollment_count', 'completion_rate', 'total_revenue')

