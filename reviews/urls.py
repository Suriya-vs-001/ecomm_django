from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_viewsets import UserReviewViewSet

router = DefaultRouter()
router.register(r'userreview', UserReviewViewSet)

urlpatterns = router.urls
