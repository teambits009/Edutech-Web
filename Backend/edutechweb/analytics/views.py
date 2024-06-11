# Create your views here.
from rest_framework import viewsets
from .models import CourseAnalytics
from .serializers import CourseAnalyticsSerializer

class CourseAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = CourseAnalytics.objects.all()
    serializer_class = CourseAnalyticsSerializer

