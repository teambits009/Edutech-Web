from django.db import models
from courses.models import Course

class CourseAnalytics(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='analytics')
    enrollment_count = models.IntegerField(default=0)
    completion_rate = models.FloatField(default=0.0)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

