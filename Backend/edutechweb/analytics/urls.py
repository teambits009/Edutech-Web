from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseAnalyticsViewSet

router = DefaultRouter()
router.register(r'course-analytics', CourseAnalyticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
